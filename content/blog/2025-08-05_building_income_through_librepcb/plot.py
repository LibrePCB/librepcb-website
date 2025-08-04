# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "kaleido",
#     "numpy",
#     "pandas",
#     "plotly",
# ]
# ///
import plotly.graph_objects as go
import pandas as pd

data = {
    'Year': [2019, 2020, 2021, 2022, 2023, 2024],
    'Full-Time Job': [100, 100, 100, 92, 0, 0],
    'Freelance Work': [0, 0, 0, 0, 8, 15],
    'LibrePCB': [1, 1, 1, 3, 34, 41],
}
df = pd.DataFrame(data)

colors = {
    'Full-Time Job': '#636efa',
    'Freelance Work': '#ef553b',
    'LibrePCB': '#29d682'
}

fig = go.Figure()

for category in ['LibrePCB', 'Freelance Work', 'Full-Time Job']:
    fig.add_trace(go.Bar(
        x=df['Year'],
        y=df[category],
        name=category,
        marker=dict(color=colors[category]),
    ))

fig.add_vrect(x0=2018.6, x1=2022.2,  # offset because year bars are centered
              annotation_text="Employed", annotation_position="top",
              fillcolor="#636efa", opacity=0.2, line_width=0, layer="below")

fig.add_vrect(x0=2022.8, x1=2023.8,  # offset because year bars are centered
              annotation_text="NLnet Grant 1", annotation_position="top",
              fillcolor="yellow", opacity=0.5, line_width=0, layer="below")

fig.add_vrect(x0=2024.2, x1=2025.2,  # offset because year bars are centered
              annotation_text="NLnet Grant 2", annotation_position="top",
              fillcolor="yellow", opacity=0.5, line_width=0, layer="below")

fig.add_vline(
    x=2023.3, y0=0, y1=0.8, line_dash="dot",
    label=dict(
        text="LibrePCB 1.0.0",
        textposition="end",
        textangle=0,
        yanchor="bottom",
    ),
)

fig.add_vline(
    x=2023.8, y0=0, y1=0.7, line_dash="dot",
    label=dict(
        text="LibrePCB 1.1.0",
        textposition="end",
        textangle=0,
        yanchor="bottom",
    ),
)

fig.add_vline(
    x=2024.4, y0=0, y1=0.6, line_dash="dot",
    label=dict(
        text="LibrePCB 1.2.0",
        textposition="end",
        textangle=0,
        yanchor="bottom",
    ),
)

fig.update_layout(
    barmode='stack',
    template='plotly_white',
    xaxis=dict(tickmode='array', tickvals=df['Year']),
    yaxis=dict(gridcolor='LightGray'),
    yaxis_range=[0, 115],
    yaxis_ticksuffix="%",
    margin=dict(l=20, r=20, t=20, b=20),
)

fig.write_image("income-distribution.png", width=800, height=300)
