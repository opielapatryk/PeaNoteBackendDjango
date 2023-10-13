from django.test import TestCase

# Create your tests here.
from main.models import User, Sticker

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='joedoe', password='goodjoe', email='joe@doe.com')
        User.objects.create(username='joesfriend', password='rossfriend', email='ross@thefriend.com')
        
    def test_user_succesfully_created(self):
        user = User.objects.get(username='joedoe')
        self.assertEqual(user.username, 'joedoe')

    def test_add_friend(self):
        user = User.objects.get(username='joedoe')
        friend = User.objects.get(username='joesfriend')
        
        user.friends.add(friend)

        self.assertEqual(user.friends.count(), 1)


class StickerTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='joedoe', password='goodjoe', email='joe@doe.com')
        Sticker.objects.create(content='foo',creator=User.objects.get(username='joedoe'))
    
    def test_sticker_succesfully_created(self):
        creator = User.objects.get(username='joedoe')
        target = User.objects.create(username='targetUser',password='targetPassword', email='target@user.com')
        sticker = Sticker.objects.get(creator=creator)

        target.stickersOnBoard.add(sticker)
        self.assertEqual(target.stickersOnBoard.count(), 1)