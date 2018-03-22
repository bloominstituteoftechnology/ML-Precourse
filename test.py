import unittest
import precourse

class UnitTests(unittest.TestCase):
    def test_f(self):
        # Failure message: 
        # f(x) does not return x squared
        message = "f(x) does not return x squared"
        self.assertEqual(precourse.f(1),1, msg=message)
        self.assertEqual(precourse.f(5),25, msg=message)
        self.assertEqual(precourse.f(-5),25, msg=message)
    def test_f_2(self):
        message =  "f_2(x) does not return x cubed"
        self.assertEqual(precourse.f_2(1),1,msg=message)
        self.assertEqual(precourse.f_2(5),125,msg=message)
        self.assertEqual(precourse.f_2(-5),-125,msg=message)
    def test_f_3(self):
        # Failure message: 
        message =  'f_3(x) does not return x cubed plus 5x'
        self.assertEqual(precourse.f_3(1),6,msg=message)
        self.assertEqual(precourse.f_3(5),130,msg=message)
        self.assertEqual(precourse.f_3(-5),-120,msg=message)
    def test_vector_sum(self):
        # Failure message: 
        message = 'vector_sum(x,y) does not return x+y'
        self.assertEqual(precourse.vector_sum([1],[1]),[2],msg = message)
    def test_vector_less(self):
        # Failure message: 
        message = 'vector_less(x,y) does not return x-y'
        self.assertEqual(precourse.vector_less([1],[1]),[0],msg = message)
    def test_vector_magnitude(self):
        # Failure message: 
        message = 'vector_magnitude(x) does not return sqrt(sum(x_i^2)) -> the length of x'
        self.assertEqual(precourse.vector_magnitude([4,3]),5,msg = message)
        self.assertEqual(precourse.vector_magnitude([63,16]),65,msg = message)
    def test_vec5(self):
        # Failure message: 
        message = 'vec5 does not return [1,1,1,1,1]'
        import numpy as np
        self.assertTrue(np.array_equal(precourse.vec5(),[1,1,1,1,1]),msg = message)
    def test_vec3(self):
        # Failure message: 
        message = 'vec3 does not return [0,0,0]'
        import numpy as np
        self.assertTrue(np.array_equal(precourse.vec3(),[0,0,0]),msg = message)
    def test_vec2_1(self):
        # Failure message: 
        message = 'vec2_1 does not return [1,0]'
        import numpy as np
        self.assertTrue(np.array_equal(precourse.vec2_1(),[1,0]),msg = message)
    def test_vec2_2(self):
        # Failure message: 
        message = 'vec2_2 does not return [0,1]'
        import numpy as np
        self.assertTrue(np.array_equal(precourse.vec2_2(),[0,1]),msg = message)
    def test_matrix_multiply(self):
        # Failure message: 
        message = 'matrix_multiply(vec,matrix) does not multiply a 2d vec vec with a 2x2 matrix'
        import numpy as np
        self.assertTrue(np.array_equal([12,6],precourse.matrix_multiply([4,3],[[3,0],[0,2]])),msg = message)

if __name__ == '__main__':
    unittest.main()

