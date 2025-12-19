from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum, F
from analysis.models import Match, Delivery


def matches_per_year(request):
    data = (Match.objects
            .values("season")
            .annotate(matches=Count('id'))
            .order_by("season")
            )
    return JsonResponse(list(data), safe=False)


def matches_per_year_chart(request):
    return render(request, 'matches.html')


def matches_won_per_team_per_year(request):
    data = (Match.objects
            .values("season", 'winner__name')
            .annotate(wins=Count("id"))
            .order_by("season")
            )
    return JsonResponse(list(data), safe=False)


def matches_won_per_year_chart(request):
    return render(request, "matches_won.html")


def extra_runs_conceded_per_team__2016(request):
    data = (Delivery.objects
            .filter(match__season=2016)
            .values('bowling_team__name')
            .annotate(extra_runs=Sum('extra_runs'))
            .order_by('extra_runs'))

    return JsonResponse(list(data), safe=False)


def extra_runs_conceded_per_team__2016_chart(request):
    return render(request, "extra_runs_2016.html")


def top_economical_bowlers_2015(request):
    data = (
        Delivery.objects
        .filter(match__season=2015)
        .values('bowling_team__name')
        .annotate(
            total_runs=Sum('total_runs'),
            balls=Count('id')
        )
        .annotate(
            economy=F('total_runs') * 6 / F('balls')
        )
        .order_by('economy')[:10]
    )
    return JsonResponse(list(data), safe=False)


def top_economical_bowlers_2015_chart(request):
    return render(request, 'Top_10_bowler_2015.html')
