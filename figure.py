"""
figure 모듈
이 모듈은 Line 클래스와 도형의 넓이를 구하는 함수를 제공한다.
"""
import math

class Line:
    """
    클래스 Line: 선의 길이를 나타낸다.
    """
    __length = 1
    """
    __length : 선의 길이이고 기본값은 1이다. 외부에서 접근 불가능한 필드.
    """
    def __init__(self, length = 1):
        """
        __init__(length=1): Line 객체를 초기화시켜준다. 
        """
        if( (type(length) == int or type(length) == float) and length>0 ):
            self.__length = length
        
        
    def set_length(self, length):
        """
        set_length : _length 변수의 값을 외부가 원하는 값으로 변경시켜준다.
        """
        if( (type(length) == int or type(length) == float) and length>0 ):
            self.__length = length
        
    def get_length(self):
        """
        get_length: __length 변수에 저장된 값을 외부에 리턴해준다.
        """
        return self.__length

        
def area_square(line):
    square_area = line.get_length() * line.get_length()
    """ 길이를 입력받아 정사각형 넓이를 구하는 함수이다.
    Args: 매개변수를 나열한다. 
        line (Line): 한 변의 길이이다.
    Returns:
        int or float: 정사각형의 넓이를 반환합니다.
    """
    print(type(line))
    if isinstance(line, Line):
        return square_area
    else:
        return 0
    """
    매개변수의 타입이 Line 클래스가 아닌 경우 0을 반환
    """

def area_circle(line):
    """ 길이를 입력받아 원의 넓이를 구하는 함수이다. 
    Args: 매개변수를 나열한다.
        line (Line): 반지름 길이이다. 
    Returns:
        int or float: 원의 넓이를 반환합니다.
    """
    circle_area = line.get_length() * line.get_length() * math.pi
    if isinstance(line, Line):
        return circle_area
    else:
        return 0        
    """
    매개변수의 타입이 Line 클래스가 아닌 경우 0을 반환
    """
     
def area_regular_triangle(line):
    triangle_area = line.get_length() * line.get_length() * math.sqrt(3) / 4
    """ 길이를 입력받아 정삼각형 넓이를 구하는 함수이다.
    Args: 매개변수를 나열한다. 
        line (Line): 한 변의 길이이다.
    Returns:
        int or float: 정삼각형의 넓이를 반환합니다.
    """
    if isinstance(line, Line):
        return triangle_area
    else:
        return 0
    """
    매개변수의 타입이 Line 클래스가 아닌 경우 0을 반환
    """