import datetime
import uuid
from typing import List

from models.location import Location
from models.reports import Report

__reports: List[Report] = []


async def get_reports() -> List[Report]:

    # Would be an async call here.
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(
        id=str(uuid.uuid4()),
        location=location,
        description=description,
        created_date=now)

    # Simulate saving to the DB.
    # Would be an async call here.
    __reports.append(report)

    __reports.sort(key=lambda r: r.created_date, reverse=True)

    return report
