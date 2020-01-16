from app.models import Pitch
import unittest
from app import db

class PitchModelTest(unittest.TestCase):
    '''
    test class to test behaviour of pitch class
    '''
    
    def setUp(self):
        '''
        set up method that runs before evry test
        '''
         self.user_murathe = User(username = 'murathe',password = '1122334455', email = 'murathe@gmail.com')
        
        self.new_pitch = Pitch (id = 1, pitch_title = 'pitch',pitch_content = 'pitch test' category='product')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,1)
        self.assertEquals(self.new_pitch.pitch_title,'pitch')
        self.assertEquals(self.new_pitch.pitch_content,'pitch test')
        self.assertEquals(self.new_pitch.pitch_category,'promotion')
        self.assertEquals(self.new_pitch.user,self.user_faith)
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
        
    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitches) == 1)    
    
        
        
                            