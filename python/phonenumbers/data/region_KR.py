"""Auto-generated file, do not edit by hand. KR metadata"""
from ..util import u
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KR = PhoneMetadata(id='KR', country_code=82, international_prefix='00(?:[124-68]|[37]\\d{2})',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{3,9}|8\\d{8}', possible_number_pattern='\\d{4,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2|[34][1-3]|5[1-5]|6[1-4])(?:1\\d{2,3}|[2-9]\\d{6,7})', possible_number_pattern='\\d{4,10}', example_number='22123456'),
    mobile=PhoneNumberDesc(national_number_pattern='1[0-25-9]\\d{7,8}', possible_number_pattern='\\d{9,10}', example_number='1023456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='80\\d{7}', possible_number_pattern='\\d{9}', example_number='801234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='60[2-9]\\d{6}', possible_number_pattern='\\d{9}', example_number='602345678'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='50\\d{8}', possible_number_pattern='\\d{10}', example_number='5012345678'),
    voip=PhoneNumberDesc(national_number_pattern='70\\d{8}', possible_number_pattern='\\d{10}', example_number='7012345678'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='1(?:5(?:44|66|77|88|99)|6(?:00|44|6[16]|70|88))\\d{4}', possible_number_pattern='\\d{8}', example_number='15441234'),
    emergency=PhoneNumberDesc(national_number_pattern='11[29]', possible_number_pattern='\\d{3}', example_number='112'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0(8[1-46-8]|85\\d{2})?',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['1(?:0|1[19]|[69]9|5[458])|[57]0', '1(?:0|1[19]|[69]9|5(?:44|59|8))|[57]0'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})(\\d{4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['1(?:[169][2-8]|[78]|5[1-4])|[68]0|[3-6][1-9][2-9]', '1(?:[169][2-8]|[78]|5(?:[1-3]|4[56]))|[68]0|[3-6][1-9][2-9]'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{3})(\\d)(\\d{4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['131', '1312'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['131', '131[13-9]'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['13[2-9]'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3})(\\d{4})', format=u('\\1-\\2-\\3-\\4'), leading_digits_pattern=['30'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d)(\\d{3,4})(\\d{4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['2[2-9]'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d)(\\d{3,4})', format=u('\\1-\\2'), leading_digits_pattern=['21[0-46-9]'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})', format=u('\\1-\\2'), leading_digits_pattern=['[3-6][1-9]1', '[3-6][1-9]1(?:[0-46-9])'], national_prefix_formatting_rule=u('0\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1')),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format=u('\\1-\\2'), leading_digits_pattern=['1(?:5[46-9]|6[04678])', '1(?:5(?:44|66|77|88|99)|6(?:00|44|6[16]|70|88))'], national_prefix_formatting_rule=u('\\1'), domestic_carrier_code_formatting_rule=u('0$CC-\\1'))])
