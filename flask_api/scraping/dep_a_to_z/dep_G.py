
"""
This is script for getting all the events for departments starting with letter D
"""

import requests
from bs4 import BeautifulSoup
import sys
from flask_api.scraping.DateTime import getDate, getTime, getISO
from flask_api.scraping.dep_events import all_department_links, get_dep_events
import json
import re
from datetime import datetime

def Genetics(main_url, calendar, dep):
    """Getting Cell_Biology department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'news-and-events/calendar/')
    soup = BeautifulSoup(response.content, "html.parser")
    event_links = []

    # get events links
    all_links =soup.find_all("div",{"class": "event-list-item__details"})
    try:
        for div in all_links:
            link = div.find('a').get('href').split('/genetics')[1]
            event_links.append(link)
    except:
        event_links = []

    # A function that goes to each link and gets the events details
    def get_event(link):

        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

       # title
        try:
            title = soup.find('h1', {'class': 'event-details-header__title'}).text.strip()
        except:
            title = "TBD"

            # speaker
        try:
            speaker_name = soup.find('div', {'class':'profile-list'}).text.strip()
        except:
            speaker_name = "TBD"

        # we get the time of the event
        start_date = None
        iso = None
        try:
            start_time = soup.find('span',{'class':'event-time__start-date'}).text.strip()
        except:
            start_time = "TBD"
        try:
            end_time = soup.find('span',{'class':'event-time__end-date'}).text.strip()
        except:
            end_time = "TBD"
        time = f"{start_time} - {end_time}"

        # we get the date of the event
        try:
            year = soup.find('span', {'class': {'event-date__month-year'}}).text.strip()
            date__day = soup.find('span', {'class': {'event-date__day-of-week'}}).text.strip()
            event_date__day= soup.find('span', {'class': {'event-date__day'}}).text.strip()
            date = f"{date__day} {event_date__day} {year}"
            iso = getISO(date)

        except:
            date = "TBD"
        # we get the address
        try:

            json_str =  soup.find('script', {'type': 'application/ld+json'})
            json_data = json_str.text.strip()
            event_dict = json.loads(json_data)
            address = event_dict['location']['address']['streetAddress']
            json_data = json.dumps(event_dict)

        except:
            address = "TBD"

        try:
            description = soup.find('div', {'class': 'event-details-info__description'})
        except:
            description = None

        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "speaker_title": None,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def German(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + calendar)
    soup = BeautifulSoup(response.content, "html.parser")
    # get events links
    event_links = []
    events = soup.find_all('td', class_="views-field views-field-title")
    for row in events:
        link = row.find('a').get('href')
        if link:
            event_links.append(link)


    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('title').text.strip()

        # speaker
        try:
            speaker_name = soup.find('div', {'class': 'field-name-field-speaker'}).text.split(':')[-1].strip()
        except:
            speaker_name = None

        # description
        try:
            description_tag = soup.find('div', {'class': 'field-type-text-with-summary'})
            description = description_tag.find('div', {'class': 'field-items'}).text.strip()
        except:
            description = None
        try:
            # time and date
            date_div = soup.find('div', {'class': 'field-name-field-event-time'})
            date_str = date_div.find('span', {'class': 'date-display-single'})

            if date_str.has_attr('content'):
                content_attr = date_str['content']
                iso = content_attr
                date = getDate(content_attr)
                time = getTime(content_attr)
            else:
                date_str = date_div.find('span', {'class': 'date-display-start'})
                content_attr = date_str['content']
                iso = content_attr
                date = getDate(content_attr)
                time = getTime(content_attr)
        except:
            date = "TBD"
            time = "TBD"
            iso = "TBD"
        try:

            address = soup.find('span', {'class': 'fn'}).text.strip()

        except:
            address = "TBD"



         # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "description": description,
            "speaker_title": speaker_name,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link
        }
        return event

    # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events


def Global_Affairs(main_url, calendar, dep):
    """Getting African American studies department's events"""
    # send response to calendar page
    response = requests.get(main_url + 'jackson-events/')
    soup = BeautifulSoup(response.content, "html.parser")
    # get events links
    event_links = []
    events = soup.find_all('td', class_="views-field views-field-title")
    for row in events:
        link = row.find('a').get('href')
        if link:
            event_links.append(link)

    # A function that goes to each link and gets the events details
    def get_event(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        # title
        title = soup.find('title').text.strip()

        # speaker
        try:
            speaker_name = soup.find('div', {'class': 'field-name-field-speaker'}).text.split(':')[-1].strip()
        except:
            speaker_name = None

        try:
            description_div = soup.find('section', {'class':'page-sec'})
            description = description_div.find_all('p').text.strip()
        except:
            description = None
        try:
            # time and date
            date_div = soup.find('div', {'class': 'field-name-field-event-time'})
            date_str = date_div.find('span', {'class': 'date-display-single'})

            if date_str.has_attr('content'):
                content_attr = date_str['content']
                iso = content_attr
                date = getDate(content_attr)
                time = getTime(content_attr)
            else:
                date_str = date_div.find('span', {'class': 'date-display-start'})
                content_attr = date_str['content']
                iso = content_attr
                date = getDate(content_attr)
                time = getTime(content_attr)
        except:
            date = "TBD"
            time = "TBD"
            iso = "TBD"
        try:

            address = soup.find('span', {'class': 'fn'}).text.strip()

        except:
            address = "TBD"



         # Event object as a dictionary
        event = {
            "title": title,
            "department": dep,
            "speaker": speaker_name,
            "description": description,
            "speaker_title": speaker_name,
            "date": date,
            "time": time,
            "location": address,
            "iso_date": iso,
            "link": link
        }
        return event
        # get all events for African american department
    events = get_dep_events(main_url, get_event, event_links)
    return events



department_parsers = {
"https://medicine.yale.edu/genetics/": Genetics,
"https://german.yale.edu/": German,
"https://jackson.yale.edu/": Global_Affairs

}

def get_all_events_G():
    """A function that returns all events for departments starting with letter A"""
    links = all_department_links()
    all_events = []
    calendar = "calendar"
    if links:
        for name, url in links.items():
            if url in department_parsers:
                department_parser = department_parsers[url]
                department_events = department_parser(url, calendar, name)
                all_events.extend(department_events)
        return all_events
