sentence = [
'Xe bus nào đến thành phố Huế lúc 20:00HR ?',
'Xe bus nào đến thành phố Đà Nẵng vào lúc 22:00HR ?',
'Xe bus nào đến thành phố Thành phố Hồ Chí Minh vào thời điểm 12:00HR ?',
'Xe bus nào đến thành phố Đà Nẵng thời điểm 22:00HR ?',
'Thời gian xe bus B3 từ Đà Nẵng đến Huế ?',
'Thời gian nào xe bus B3 từ Đà Nẵng đến Huế ?',
'Thời điểm xe bus B3 từ Đà Nẵng đến Huế ?',
'Thời điểm nào xe bus B3 từ Đà Nẵng đến Huế ?',
'Xe bus nào đến thành phố Hồ Chí Minh ?',
'Hãy cho biết xe bus B2 đến thành phố Hà Nội lúc mấy giờ ?',
'Hãy cho biết xe bus B2 đến thành phố Hà Nội vào lúc mấy giờ ?',
'Hãy cho biết xe bus B2 đến thành phố Hà Nội vào thời gian nào ?',
'Hãy cho biết xe bus B2 đến thành phố Hà Nội vào thời điểm nào ?'
]
expect_output = [['Xe bus', 'nào', 'đến', 'thành phố Huế', 'lúc', '20:00HR', '?'], ['Xe bus', 'nào', 'đến', 'thành phố Đà Nẵng', 'vào lúc', '22:00HR', '?'], ['Xe bus', 'nào', 'đến', 'thành phố', 'Thành phố Hồ Chí Minh', 'vào thời điểm', '12:00HR', '?'], ['Xe bus', 'nào', 'đến', 'thành phố Đà Nẵng', 'thời điểm', '22:00HR', '?'], ['Thời gian', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'], ['Thời gian nào', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'], ['Thời điểm', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'], ['Thời điểm nào', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'], ['Xe bus', 'nào', 'đến', 'thành phố Hồ Chí Minh', '?'], ['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'lúc mấy giờ', '?'], ['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'vào lúc mấy giờ', '?'], ['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'vào thời gian nào', '?'], ['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'vào thời điểm nào', '?']]

pos_tag_out = [
[('Xe bus', 'N_sub'), ('nào', 'WH'), ('đến', 'V'), ('thành phố Huế', 'Name'), ('lúc', 'P'), ('20:00HR', 'Time'), ('?', 'None')] 

[('Xe bus', 'N_sub'), ('nào', 'WH'), ('đến', 'V'), ('thành phố Đà Nẵng', 'Name'), ('vào lúc', 'P'), ('22:00HR', 'Time'), ('?', 'None')] 

[('Xe bus', 'N_sub'), ('nào', 'WH'), ('đến', 'V'), ('thành phố', 'N'), ('Thành phố Hồ Chí Minh', 'Name'), ('vào thời điểm', 'None'), ('12:00HR', 'Time'), ('?', 'None')] 

[('Xe bus', 'N_sub'), ('nào', 'WH'), ('đến', 'V'), ('thành phố Đà Nẵng', 'Name'), ('thời điểm', 'WH_time'), ('22:00HR', 'Time'), ('?', 'None')] 

[('Thời gian', 'WH_time'), ('xe bus', 'N_sub'), ('B3', 'Name_bus'), ('từ', 'P'), ('Đà Nẵng', 'Name'), ('đến', 'V'), ('Huế', 'Name'), ('?', 'None')] 

[('Thời gian nào', 'WH_time'), ('xe bus', 'N_sub'), ('B3', 'Name_bus'), ('từ', 'P'), ('Đà Nẵng', 'Name'), ('đến', 'V'), ('Huế', 'Name'), ('?', 'None')] 

[('Thời điểm', 'WH_time'), ('xe bus', 'N_sub'), ('B3', 'Name_bus'), ('từ', 'P'), ('Đà Nẵng', 'Name'), ('đến', 'V'), ('Huế', 'Name'), ('?', 'None')] 

[('Thời điểm nào', 'WH_time'), ('xe bus', 'N_sub'), ('B3', 'Name_bus'), ('từ', 'P'), ('Đà Nẵng', 'Name'), ('đến', 'V'), ('Huế', 'Name'), ('?', 'None')] 

[('Xe bus', 'N_sub'), ('nào', 'WH'), ('đến', 'V'), ('thành phố Hồ Chí Minh', 'Name'), ('?', 'None')] 

[('Hãy cho biết', 'None'), ('xe bus', 'N_sub'), ('B2', 'Name_bus'), ('đến', 'V'), ('thành phố Hà Nội', 'Name'), ('lúc mấy giờ', 'WH_time'), ('?', 'None')] 

[('Hãy cho biết', 'None'), ('xe bus', 'N_sub'), ('B2', 'Name_bus'), ('đến', 'V'), ('thành phố Hà Nội', 'Name'), ('vào lúc mấy giờ', 'None'), ('?', 'None')] 

[('Hãy cho biết', 'None'), ('xe bus', 'N_sub'), ('B2', 'Name_bus'), ('đến', 'V'), ('thành phố Hà Nội', 'Name'), ('vào thời gian nào', 'WH_time'), ('?', 'None')] 

[('Hãy cho biết', 'None'), ('xe bus', 'N_sub'), ('B2', 'Name_bus'), ('đến', 'V'), ('thành phố Hà Nội', 'Name'), ('vào thời điểm nào', 'WH_time'), ('?', 'None')] 
]