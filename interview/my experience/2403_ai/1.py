from collections import namedtuple
from typing import List

def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """ 
    

    _f = []
    _data = dict()
    for record in records:
        for _field in record._fields:
            _f.append(_field)
            _data[_field] = getattr(record, _field)
    print(_f)
    print(_data)
    Patient = namedtuple("Patient", _f)
    patient_detail = Patient(**_data)

    return patient_detail
    
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                   
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
  
print(merge(personal_details, complexion))