

# PROGRAM NO LONGER FUNCTIONAL
# The county took down the site tracking COVID cases
# 3/18/2022


import requests
import bs4
import pandas as pd
import plotly.express as px

    # Fetches the data of the website
dashboardParse = requests.get("https://mychesterfieldschools.com/covid-19-dashboard/")
dashboard = bs4.BeautifulSoup(dashboardParse.text, "html.parser")
    # Pulls the tables off the site and turns it into readable data
ADTableParse = dashboard.find("table", {"class": "ea-advanced-data-table ea-advanced-data-table-static ea-advanced-data-table-43eb34e ea-advanced-data-table-sortable ea-advanced-data-table-searchable"})
januaryTableParse = dashboard.find("table", {"class": "ea-advanced-data-table ea-advanced-data-table-static ea-advanced-data-table-154930d ea-advanced-data-table-searchable"})
februaryTableParse = dashboard.find("table", {"class": "ea-advanced-data-table ea-advanced-data-table-static ea-advanced-data-table-1c469d1 ea-advanced-data-table-sortable ea-advanced-data-table-paginated ea-advanced-data-table-searchable"})

class COVIDTracker:
    def __init__(self, school, month):
        self.school = school
        self.ADTable = pd.read_html(str(ADTableParse))[0]
        self.januaryTable = pd.read_html(str(januaryTableParse))[0]
        self.februaryTable = pd.read_html(str(februaryTableParse))[0]
        self.table = pd.concat([self.januaryTable, self.ADTable, self.februaryTable], axis=0)
        schoolCases = self.table.query(f"Location in ('{self.school} (Student)', '{self.school} (Staff)')")
        self.caseCount = schoolCases.groupby("Date").size()
        if month == "AD":
            self.month = self.ADTable
        elif month == "January":
            self.month = self.januaryTable
        elif month == "February":
            self.month = self.februaryTable
    def totalCases(self):
        plotPoints = pd.DataFrame(self.caseCount, columns = ["Cases"])
        plotPoints = plotPoints.cumsum()
        plotPoints["Case Date"] = plotPoints.index
        plotPoints["Case Date"] = pd.to_datetime(plotPoints["Case Date"])
        plotPoints = plotPoints.sort_values(by='Case Date')
        table = px.line(plotPoints, x="Case Date", y="Cases")
        table.show()
    def casesPerDay(self):
        plotPoints = pd.DataFrame(self.caseCount, columns = ["Cases"])
        plotPoints["Case Date"] = plotPoints.index
        plotPoints["Case Date"] = pd.to_datetime(plotPoints["Case Date"])
        plotPoints = plotPoints.sort_values(by='Case Date')
        table = px.line(plotPoints, x="Case Date", y="Cases")
        table.show()
    def casesByMonth(self):
        checkMonth = self.month.query(f"Location in ('{self.school} (Student)', '{self.school} (Staff)')")
        checkMonth = checkMonth.groupby("Date").size()
        plotPoints = pd.DataFrame(checkMonth, columns = ["Cases"])
        plotPoints["Case Date"] = plotPoints.index
        plotPoints["Case Date"] = pd.to_datetime(plotPoints["Case Date"])
        plotPoints = plotPoints.sort_values(by='Case Date')
        table = px.line(plotPoints, x="Case Date", y="Cases")
        table.show()

cloverHillElem = COVIDTracker("Clover Hill Elementary School", "AD")