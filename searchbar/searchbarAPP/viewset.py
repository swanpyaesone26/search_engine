from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from searchbarAPP.models import Movie

class MovieViewSet(viewsets.ViewSet):
    queryset = Movie.objects.all()

    @action(detail=False, methods=['get'])
    def searching(self, request):
        search_term = request.query_params.get('name', None)

        if search_term:
            # Ensure the search term is properly formatted (e.g., strip any leading/trailing spaces)
            search_term = search_term.strip()

            with connection.cursor() as cursor:
                # Using raw SQL to perform full-text search and return relevant columns
                cursor.execute(
                    """
                    SELECT "Title", "Release Year", "Wiki Page", "Plot", ts_rank_cd(search_vector, plainto_tsquery('english', %s)) AS rank
                    FROM "Movie"
                    WHERE search_vector @@ plainto_tsquery('english', %s)
                    ORDER BY rank DESC;
                    """,
                    [search_term, search_term]
                )

                rows = cursor.fetchall()

            # Convert the raw query result to a list of dictionaries, including relevant columns
            movies = [
                {
                    'title': row[0],
                    'release_year': row[1],
                    'wiki_page': row[2],
                    'plot': row[3],
                    'rank': row[4]
                }
                for row in rows
            ]

            return Response(movies)

        return Response({'error': 'Name parameter is required'}, status=400)
