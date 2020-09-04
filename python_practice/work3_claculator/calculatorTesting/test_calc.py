import pytest
import yaml
from HogwartsLG3.python_practice.work3_claculator.calculatorTesting.calculator import Calculator

'''
pytest 命名规则
文件名：以 test_开头 (test_*.py)
类名：以 Test 开头
方法名：以test_开头
'''

#读取测试数据
def get_datas():
    with  open('./datas/calc.yml',encoding='utf-8') as f:
    #打开文件，如果是有中文的文件，需要加encoding=”utf"
        mydatas = yaml.safe_load(f)
        #加法正确数据
        add_datas_correct = mydatas['add_correct']['add_datas_correct']
        add_correct_ids = mydatas['add_correct']['add_myids_correct']
        #加法错误数据
        add_mistake_datas = mydatas['add_mistake']['add_mistake_datas']
        add_mistake_ids = mydatas['add_mistake']['add_mistake_ids']

        div_datas_correct  = mydatas['div_correct']['div_datas_correct']
        div_ids_correct = mydatas['div_correct']['div_ids_correct']

        div_datas_mistake = mydatas['div_mistake']['div_datas_mistake']
        div_ids_mistake = mydatas['div_mistake']['div_ids_mistake']

    return [add_datas_correct,add_correct_ids,add_mistake_datas,add_mistake_ids,div_datas_correct,div_ids_correct,
            div_datas_mistake,div_ids_mistake]

class TestCalc:
    @pytest.mark.add
    def setup_class(self):
        print("\n类开始时，开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n类结束时，结束计算")

    def set_up(self):
        print("\n开始计算")

    def tear_down(self):
        print("\n结束计算")

    @pytest.mark.add_correct
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add_correct(self,a,b,expect):
        '''
        测试相加
        '''
        #calc = Calculator()
        result = round(self.calc.add(a,b),2)
        assert expect == result
        print("测试相加正确情况")

    @pytest.mark.add_mistake
    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_add_mistake(self, a, b, expect):
        # calc = Calculator()
        result = round(self.calc.add(a, b),2)
        assert expect == result
        print("测试相加错误的情况")
    # # @pytest.mark.parametrize('a,b,expect',[
    # #     (0.1,0.1,0.2),
    # #     (0.1, 0.2, 0.3),
    # # ])
    # def test_add_float(self,a,b,expect):
    #     result = round(self.calc.add(a,b),expect)
    #     assert expect == result


    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect',get_datas()[4], ids=get_datas()[5])
    def test_div_correct(self, a, b, expect):
        print("测试相除")
        # calc = Calculator()
        result = round(self.calc.div(a, b),2)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()[6], ids=get_datas()[7])
    def test_div_mistake(self, a, b, expect):
        '''
        测试相除
        '''
        print("测试相除")
        # calc = Calculator()
        result = round(self.calc.div(a, b),2)
        assert expect == result
