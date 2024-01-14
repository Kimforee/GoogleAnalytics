
import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import Calls, Messages, PeopleAskedForDirection, WebsiteVisitsFromProfile, ProfileViews, SearchesAppearance

def generate_dummy_data():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for month in months:
        Calls.objects.create(month=month, count=random.randint(20, 50), percentage_change=random.randint(-10, 10))
        Messages.objects.create(month=month, count=random.randint(0, 10))
        PeopleAskedForDirection.objects.create(month=month, count=random.randint(10, 30), percentage_change=random.randint(-20, 20))
        WebsiteVisitsFromProfile.objects.create(month=month, count=random.randint(30, 70), percentage_change=random.randint(-30, 30))
        ProfileViews.objects.create(month=month, count=random.randint(800, 1200), percentage_change=random.randint(50, 100))
        SearchesAppearance.objects.create(month=month, count=random.randint(50, 150), percentage_change=random.randint(100, 300))

def generate_report(month):
    report = {}

    # report['Calls'] = {'count': Calls.objects.get(month=month).count, 'percentage_change': Calls.objects.get(month=month).percentage_change}
    # report['Messages'] = {'count': Messages.objects.get(month=month).count}
    # report['PeopleAskedForDirection'] = {'count': PeopleAskedForDirection.objects.get(month=month).count, 'percentage_change': PeopleAskedForDirection.objects.get(month=month).percentage_change}
    # report['WebsiteVisitsFromProfile'] = {'count': WebsiteVisitsFromProfile.objects.get(month=month).count, 'percentage_change': WebsiteVisitsFromProfile.objects.get(month=month).percentage_change}
    # report['ProfileViews'] = {'count': ProfileViews.objects.get(month=month).count, 'percentage_change': ProfileViews.objects.get(month=month).percentage_change}
    # report['SearchesAppearance'] = {'count': SearchesAppearance.objects.get(month=month).count, 'percentage_change': SearchesAppearance.objects.get(month=month).percentage_change}

    # Calls
    calls_records = Calls.objects.filter(month=month)
    if calls_records.exists():
        report['Calls'] = {'count': calls_records[0].count, 'percentage_change': calls_records[0].percentage_change}

    # Messages
    messages_records = Messages.objects.filter(month=month)
    if messages_records.exists():
        report['Messages'] = {'count': messages_records[0].count}

    # People Asked for Direction
    direction_records = PeopleAskedForDirection.objects.filter(month=month)
    if direction_records.exists():
        report['PeopleAskedForDirection'] = {'count': direction_records[0].count, 'percentage_change': direction_records[0].percentage_change}

    # Website Visits from Profile
    website_records = WebsiteVisitsFromProfile.objects.filter(month=month)
    if website_records.exists():
        report['WebsiteVisitsFromProfile'] = {'count': website_records[0].count, 'percentage_change': website_records[0].percentage_change}

    # Profile Views
    profile_views_records = ProfileViews.objects.filter(month=month)
    if profile_views_records.exists():
        report['ProfileViews'] = {'count': profile_views_records[0].count, 'percentage_change': profile_views_records[0].percentage_change}

    # Searches Appearance
    searches_records = SearchesAppearance.objects.filter(month=month)
    if searches_records.exists():
        report['SearchesAppearance'] = {'count': searches_records[0].count, 'percentage_change': searches_records[0].percentage_change}

    return report


def consolidate_report():
    # Choose the month for the report
    report_month = 'January'  # You can change this to the desired month

    # Generate and populate dummy data
    generate_dummy_data()

    # Generate the report for the chosen month
    report = generate_report(report_month)

    return report

def index(request):
    # Consolidate the report
    consolidated_report = consolidate_report()
    return render(request, 'index.html', {'report': consolidated_report})

    # return JsonResponse(consolidated_report)  
