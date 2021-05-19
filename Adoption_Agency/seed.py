from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name="Isaac Mewton",species="cat", photo_url='https://cardfool.s3.amazonaws.com/cards/assets/low_Cat%20Hug%20Easter_cover.jpg', age=1, notes="Loves to destroy shoes and furniture. Generally dislikes humans.")
p2 = Pet(name="Pug-Zilla",species="dog", photo_url='https://www.petguide.com/wp-content/uploads/2018/07/funniest-dog-breeds-pug.jpg', age=6, notes="Lookin' for Pug in all the wrong places.", available=False)
p3 = Pet(name="Alanis Mare-issette",species="cat", photo_url='https://i.pinimg.com/originals/57/51/ab/5751ab5082e364477876a999b688a8b5.jpg', age=7, notes="Isn't it ironic?", available=True)
p4 = Pet(name="Marty McFly",species="porcupine", photo_url='https://www.torontozoo.com/img/1200/20190415031412301SecretaryBird.jpg', age=13, notes="Where this bird's going, he doesn't need roads.", available=True)
p5 = Pet(name="Nick Furry",species="dog", photo_url='https://i.pinimg.com/originals/00/e1/a6/00e1a664d5da598a71d744da5d2058d2.jpg', age=13, notes="Usually busy assembling the Avengers.", available=True)
p6 = Pet(name="Marlin",species="cat", photo_url='https://cdn.mos.cms.futurecdn.net/4UdEs7tTKwLJbxZPUYR3hF-1200-80.jpg', age=6, notes="Always looking for Nemo.", available=False)

db.session.add_all([p1, p2, p3, p4, p5, p6])
db.session.commit()


