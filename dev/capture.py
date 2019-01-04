#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from librepcb import LibrePcb
from api_server import ApiServer
from screenshot import Screenshot
from screencast import Screencast


def library_manager_gif():
    api = ApiServer()
    with LibrePcb() as app:
        control_panel = app.funq.widget('controlPanel')
        app.set_widget_size(control_panel, 800, 600)
        app.remove_version_number_from_window_title(control_panel)
        app.fake_workspace_path_in_control_panel()
        time.sleep(2.0)  # wait until the library scan has finished
        app.hide_no_libraries_warning_in_control_panel()
        with Screencast() as c:
            c.set_cursor_pos(500, 300)
            with Screenshot.window(control_panel) as s:
                c.add_screenshot(s, 0.3, cursor=True)

            # Click on "Library Manager" button in control panel
            btn = app.funq.widget('controlPanelOpenLibraryManagerButton')
            props = btn.properties()
            pos = btn.map_pos_to(props['width'] / 2, props['height'] / 2,
                                 control_panel)
            c.move_cursor(pos[0], pos[1])
            c.cursor_click()
            btn.click()

            # Load libraries
            library_manager = app.funq.widget('libraryManager')
            app.set_widget_size(library_manager, 800, 600)
            for i in range(10):
                with Screenshot.window(library_manager) as s:
                    c.add_screenshot(s, 0.07, cursor=True)
                    api.process()
                    time.sleep(0.5)

            # Select libraries
            libs = [0, 1, 2, 5, 6]
            for i in libs:
                suffix = "-{}".format(i) if i > 0 else ''
                path = app.funq.aliases['libraryManagerDownloadFromRepoLibraryListItem'] + suffix
                cbx = app.funq.widget(path=path + '::cbxDownload')
                props = cbx.properties()
                box_pos_y = props['height'] / 2
                box_pos_x = props['width'] - box_pos_y
                pos = cbx.map_pos_to(box_pos_x, box_pos_y, library_manager)
                c.move_cursor(pos[0], pos[1])
                c.add_delay(0.2)
                cbx.set_property('checked', True)
                time.sleep(0.3)  # workaround for some glitches
                with Screenshot.window(library_manager) as s:
                    c.add_screenshot(s, 0.2, cursor=True)

            # Download libraries
            library_list = app.funq.widget('libraryManagerInstalledLibrariesList')
            btn = app.funq.widget('libraryManagerDownloadFromRepoDownloadButton')
            props = btn.properties()
            pos = btn.map_pos_to(props['width'] / 2, props['height'] / 2,
                                 library_manager)
            c.move_cursor(pos[0], pos[1])
            c.cursor_click()
            btn.click()
            while True:
                loaded_libs = len(library_list.model_items().items)
                last_frame = loaded_libs == len(libs) + 1
                if last_frame:
                    time.sleep(0.5)  # workaround for missing last frame...
                with Screenshot.window(library_manager) as s:
                    c.add_screenshot(s, 0.1, cursor=True)
                    api.process()
                    time.sleep(0.1)
                if last_frame:
                    break
            c.add_delay(4.0)

            # Save the GIF
            c.save('library_manager.gif')


if __name__ == "__main__":
    library_manager_gif()
