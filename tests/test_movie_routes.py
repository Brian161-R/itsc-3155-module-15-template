from flask.testing import FlaskClient

from src.models import Movie, db

def test_get_all_movies(test_app: FlaskClient):
    
    test_movie = Movie(title = 'Avatar', director='James Cameron', rating=5)
    db.session.add(test_movie)
    db.session.commit()

    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    assert res.status_code == 200
    assert f'<td><a href="/movies/{test_movie.movie_id}">Avatar</a></td>' in page_data
    assert '<td>James Cameron</td>' in page_data
    assert '<td>5</td>' in page_data





