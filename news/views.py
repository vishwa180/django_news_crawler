from core.views import JSONApi
from news.models import NewsArticle
from django.core.paginator import Paginator
from rest_framework.response import Response


class NewsView(JSONApi):
    @JSONApi.api
    def get(self, request):
        query_params = request.GET

        # constructing the filters
        filters = dict()
        if "keyword" in query_params:
            filters["title__icontains"] = query_params["keyword"]

        # fetching the news articles from database
        new_articles = list(NewsArticle.objects.filter(**filters)
                            .values("title", "created_at", "url")
                            .order_by("created_at"))

        # creating a pages object
        pages = Paginator(new_articles, 30)

        # check is page_number is provided in query_params
        current_page = int(query_params["page"]) if "page" in query_params else 1

        return Response(data={
            "new_articles": pages.page(current_page).object_list,
            "count_per_page": 30,
            "current_page": current_page,
            "total_pages": pages.num_pages
        })
