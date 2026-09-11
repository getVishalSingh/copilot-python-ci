#use pytest to test the add function
import pytest
from app import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

#add main function to run pytest
if __name__ == "__main__":
    pytest.main()
