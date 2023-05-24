import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
month_average = data.groupby(["Month"]).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Month',
        align: 'center'
    },
    subtitle: {
        text: 'According to 45,000 reviews',
        align: 'center'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Start to Finish'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}/5.0'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Month {point.x}: {point.y}/5.0'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def course_review():
    web_page = jp.QuasarPage()

    h1 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=web_page, text="These graphs represent course review analysis.", classes="text-h5 text-center q-pa-md")

    hc = jp.HighCharts(a=web_page, options=chart_def)
    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average["Rating"])

    return web_page

jp.justpy(course_review)