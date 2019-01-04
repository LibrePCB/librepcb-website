#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import platform
import shutil
import tempfile
import funq
import time
from funq.client import ApplicationContext, ApplicationConfig
from funq.errors import FunqError
from config import config


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')


class GlobalOptions:
    def __init__(self):
        self.funq_conf = 'funq.conf'
        self.funq_attach_exe = funq.tools.which('funq')
        self.funq_gkit = 'default'
        self.funq_gkit_file = os.path.join(os.path.dirname(
            os.path.realpath(funq.client.__file__)), 'aliases-gkits.conf')


class LibrePcb:
    def __init__(self, projects=True):
        # Copy test data to temporary directory to avoid modifications in
        # original data
        self._tmp = tempfile.mkdtemp()
        self._data = os.path.join(self._tmp, 'data')
        shutil.copytree(DATA_DIR, self._data)
        self._workspace = os.path.join(self._data, 'workspace')
        self._projects = os.path.join(self._workspace, 'projects')
        if projects:
            shutil.copytree(os.path.join(self._data, 'projects'), self._projects)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self._context
        shutil.rmtree(self._tmp)

    def abspath(self, relpath):
        return os.path.join(self._data, relpath)

    @property
    def funq(self):
        return self._context.funq

    def open(self):
        self._create_application_config_file()
        cfg = ApplicationConfig(executable=config['LIBREPCB_EXECUTABLE'],
                                args=(),
                                cwd=os.getcwd(),
                                env=self._env(),
                                aliases=config['LIBREPCB_ALIASES'],
                                global_options=GlobalOptions())
        self._context = ApplicationContext(cfg)

    def set_widget_size(self, widget, width, height):
        widget.set_properties(
            minimumWidth=width,
            maximumWidth=width,
            minimumHeight=height,
            maximumHeight=height,
            x=0,
            y=0
        )
        time.sleep(0.3)  # changing window size takes some time

    def fake_workspace_path_in_control_panel(self):
        lbl = self.funq.widget('controlPanelStatusBarWorkspaceLabel')
        lbl.set_property('text', 'Workspace: /home/me/librepcb-workspace')

    def remove_version_number_from_window_title(self, window):
        title = window.properties()['windowTitle']
        title = re.sub(r'\d+\.\d+(\.\d+)?(\-\w+)?', '', title)
        window.set_property('windowTitle', title)

    def hide_no_libraries_warning_in_control_panel(self):
        lbl = self.funq.widget('controlPanelWarnForNoLibrariesLabel', wait_active=False)
        lbl.set_property('visible', False)

    def _create_application_config_file(self):
        ini = os.path.join(self._data, 'config', 'LibrePCB', 'LibrePCB.ini')
        with open(ini, 'a') as f:
            f.write("[workspaces]\n")
            f.write("most_recently_used=\"{}\"\n".format(
                self._workspace.replace('\\', '/')))

    def _env(self):
        env = os.environ
        # Make GUI independent from the system's language
        env['LC_ALL'] = 'C'
        # Override configuration location
        env['LIBREPCB_CONFIG_DIR'] = os.path.join(self._data, 'config')
        # Use a neutral username
        env['USERNAME'] = 'librepcb'
        # Force LibrePCB to use Qt-style file dialogs
        env['LIBREPCB_DISABLE_NATIVE_DIALOGS'] = '1'
        return env
