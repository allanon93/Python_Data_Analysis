import pandas
from datetime import datetime
from pytz import utc
import justpy as jp

data = pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name']).mean().unstack()

chart_def = """
{

    title: {
        text: 'U.S Solar Employment Growth by Job Category, 2010-2020',
        align: 'left'
    },

    subtitle: {
        text: 'Source: <a href="https://irecusa.org/programs/solar-jobs-census/" target="_blank">IREC</a>',
        align: 'left'
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
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            }
        }
    },

    series: [{
        name: 'Installation & Developers',
        data: [43934, 48656, 65165, 81827, 112143, 142383,
            171533, 165174, 155157, 161454, 154610]
    }, {
        name: 'Manufacturing',
        data: [24916, 37941, 29742, 29851, 32490, 30282,
            38121, 36885, 33726, 34243, 31050]
    }, {
        name: 'Sales & Distribution',
        data: [11744, 30000, 16005, 19771, 20185, 24377,
            32147, 30912, 29243, 29213, 25663]
    }, {
        name: 'Operations & Maintenance',
        data: [null, null, null, null, null, null, null,
            null, 11164, 11218, 10077]
    }, {
        name: 'Other',
        data: [21908, 5548, 8105, 11248, 8989, 11816, 18274,
            17300, 13053, 11906, 10073]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

}
"""

def course_review():

    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of Course Reviews",
    classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=web_page, text="These graphs represent course review analysis.")

    hc = jp.HighCharts(a=web_page, options=chart_def)

    hc.options.xAxis.categories = list(month_average_crs.index)

    hc_data = [{"name": v0, "data": [v1 for v1 in month_average_crs[v0]]}
    for v0 in month_average_crs.columns]

    hc.options.series = hc_data

    return web_page

jp.justpy(course_review)