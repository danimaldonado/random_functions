"""Random functions that plot things.

"""

import pandas as pd
import plotly.graph_objects as go


def scatter_plot_with_multiple_variables(dataframe, x, y, case_name, cases, title):
    """Creates a figure with several variables with menu.

    Args:
        dataframe (pd.DataFrame): Dataframe to plot x vs y.
        x (Str): x-axis data name.
        y (Str): y-axis data name.
        case_name (Str): Defines the clase name, i.e., 'country'
        cases (List[Str]): Different features to plot the (x, y)
            simultaneously, i.e., a list of countries: ['Italy', 'UK', ...]
        title (Str): Figure title

    """

    fig = go.Figure()

    temp_list = [dict(label='All features',
                      method='update',
                      args=[{'visible': [True for item in cases]}])]

    for i, case in enumerate(cases):
        data = dataframe[dataframe[case_name] == case][[x, y]]

        temp_dict = dict(label='{}'.format(case),
                         method='update',
                         args=[{'visible': [True if j == i else False for j,
                                                                          item in
                                            enumerate(case)]}])

        temp_list.append(temp_dict)

        fig.add_trace(go.Scatter(x=data[x],
                                 y=data[y],
                                 name='{}'.format(case)))

    fig.update_layout(title_text=title,
                      updatemenus=[dict(active=0,
                                        buttons=temp_list)],
                      xaxis=dict(title=x,
                                 tickangle=-60))

    fig.show()
