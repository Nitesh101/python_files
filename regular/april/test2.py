str = [("Rakesh","Python",88),("Lavanya","Django",91),("Balram","Flask",72),    ("Vineeth","Zope",73),("Harsha","Scrapy",99),("Manjeera","Python",81),("Kishore","Django",93)]
sta =sorted([i for i in str if i[1] == 'Django'],key=lambda x:x[1])
print sta

