# import unittest
# from app.models import Comment,Pitch,User
# from app import db


# class TestPitch(unittest.TestCase):
#     def setUp(self):
#         self.new_pitch = Pitch(content="pitcher",category="Business")
#         self.new_comment = Comment(comment = "comment",pitch=self.new_pitch)

#     def tearDown(self):
#         db.session.delete(self)
#         User.query.commit()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_comment.comment,"comment"))

#     def test_check_instance_variables(self):
