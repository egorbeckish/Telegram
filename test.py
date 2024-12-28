from hotpdf import HotPdf

pdf = HotPdf(open("PDF Results/1500 freestyle Men's Heats.pdf", 'rb')).extract_text(*[0, 200, 525, 510], 1).split('\n')
print(pdf)
