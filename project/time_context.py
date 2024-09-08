import datetime

def get_datetime_now(request):
    
    year = datetime.date.today().year
    
    return {'year_now': year}


