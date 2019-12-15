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
expect_output = [
['Xe bus', 'nào', 'đến', 'thành phố Huế', 'lúc 20:00HR', '?'],
['Xe bus', 'nào', 'đến', 'thành phố Đà Nẵng', 'vào lúc 22:00HR', '?'],
['Xe bus', 'nào', 'đến', 'thành phố', 'Thành phố Hồ Chí Minh', 'vào thời điểm 12:00HR', '?'],
['Xe bus', 'nào', 'đến', 'thành phố Đà Nẵng', 'thời điểm 22:00HR', '?'],
['Thời gian', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'],
['Thời gian nào', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'],
['Thời điểm', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'],
['Thời điểm nào', 'xe bus', 'B3', 'từ', 'Đà Nẵng', 'đến', 'Huế', '?'],
['Xe bus', 'nào', 'đến', 'thành phố Hồ Chí Minh', '?'],
['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'lúc mấy giờ', '?'],
['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'vào lúc mấy giờ', '?'],
['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'vào thời gian nào', '?'],
['Hãy cho biết', 'xe bus', 'B2', 'đến', 'thành phố Hà Nội', 'vào thời điểm nào', '?']
]