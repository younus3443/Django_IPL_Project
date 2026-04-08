from django.urls import path, include
from . import views

urlpatterns = [
    
    #api routes
    path("matches-per-year/", views.matches_per_year, name="matches_per_year"),
    path("matches-won-per-year/",views.matches_won_per_team_per_year,name="matches-won-per-year"),
    path("extra-runs-2016/",views.extra_runs_conceded_per_team__2016,name="extra_runs_conceded_per_team__2016"),
    path("top-10-bowler-2015/",views.top_economical_bowlers_2015,name="top_economical_bowlers_2015"),
    
    #charts routes
    path("matches-per-year-chart/",views.matches_per_year_chart,name="matches_per_year_chart"),
    path("matches-won-per-year-chart/",views.matches_won_per_year_chart,name="matches_won_per_year_chart"),
    path("extra-runs-2016-chart/",views.extra_runs_conceded_per_team__2016_chart,name="extra_runs_conceded_per_team__2016_chart"),
    path("top-10-bowler-2015-chart/",views.top_economical_bowlers_2015_chart,name="top_economical_bowlers_2015_chart")
]
