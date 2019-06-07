from datetime import datetime
from django.core.paginator import EmptyPage, Paginator

import pytz


def convert_date(str_date: str) -> datetime:
    date = datetime.strptime(str_date.strip(), '%Y-%m-%d %H:%M:%S')
    return pytz.utc.localize(date)


def normalize_email(email: str) -> str:
    from colossus.apps.subscribers.models import Subscriber
    return Subscriber.objects.normalize_email(email)


def normalize_text(text: str) -> str:
    if text is None:
        return ''
    text = str(text)
    text = ' '.join(text.split())
    return text


def paginate(request, items, amount):
    """ Paginate queryset with latest published item.
    """
    paginator = Paginator(items.order_by('-date'), amount)

    try:
        page_number = int(request.GET['page'])
        page = paginator.page(page_number)
    except (ValueError, KeyError, EmptyPage):
        page = paginator.page(1)

    return paginator, page
