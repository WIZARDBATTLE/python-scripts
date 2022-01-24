import requests
import bs4
import pandas as pd
import plotly.express as px

# Fetches the data of the website
dashboardParse = requests.get("https://mychesterfieldschools.com/covid-19-dashboard/")
dashboard = bs4.BeautifulSoup(dashboardParse.text, "html.parser")
# Pulls the tables off the site and turns it into readable data
tableParse = dashboard.find("table", {"class": "ea-advanced-data-table ea-advanced-data-table-static ea-advanced-data-table-154930d ea-advanced-data-table-searchable"})
tableParse2 = dashboard.find("table", {"class": "ea-advanced-data-table ea-advanced-data-table-static ea-advanced-data-table-43eb34e ea-advanced-data-table-sortable ea-advanced-data-table-searchable"})
table1 = pd.read_html(str(tableParse))[0]
table2 = pd.read_html(str(tableParse2))[0]
table = pd.concat([table1, table2], axis=0)
# Finds Clover Hill only cases and organizes them by date
cloverHillCases = table.query("Location in ('Clover Hill Elementary School (Student)', 'Clover Hill Elementary School (Staff)')")
caseCount = cloverHillCases.groupby("Date").size()

# Turns the data into a table sorted by date
plotPoints = pd.DataFrame(caseCount, columns=["Cases"])
plotPoints["Case Date"] = plotPoints.index
plotPoints["Case Date"] = pd.to_datetime(plotPoints["Case Date"])
plotPoints = plotPoints.sort_values(by='Case Date')
cHtable = px.line(plotPoints, x="Case Date", y="Cases")
