from rest_framework.response import Response
from rest_framework.decorators import api_view
from caisse.services.domain_service import DomainService 
from caisse.models import engine
from sqlalchemy.orm import sessionmaker
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import cache_page

Session = sessionmaker(bind=engine)

@cache_page(60 * 15, key_prefix='get_performances')
@api_view(['GET'])
def performances(request):
    import time
    time.sleep(2)
    session = Session()
    service = DomainService(session)
    performances_data = service.performances()
# Convert generator/zip to list of dicts for JSON
    result = []
    for total, stocks, store_id in performances_data:
        result.append({
            'store_id': store_id,
            'total_sales': total,
            'stocks': [
                {'product_id': stock.product, 'quantity': stock.quantite} for stock in stocks
            ] if stocks else []
        })
    return Response(result)

@cache_page(60 * 15, key_prefix='get_report')
@api_view(['GET'])
def report(request, store_id):
    import time 
    time.sleep(2)
    session = Session()
    service = DomainService(session)
    report = service.generate_report(store_id)
    # You may want to serialize sales and most_sold_product if needed
    # For now, just convert to dict with IDs and values
    report_data = {
        'store_id': report['store_id'],
        'sales': [sale.id for sale in report['sales']],
        'most_sold_product': getattr(report['most_sold_product'], 'id', None) if report['most_sold_product'] else None,
        'max_quantity': report['max_quantity']
    }
    return Response(report_data)