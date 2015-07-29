text = "X-DSPAM-Confidence:    0.8475";
num = text.find(':')
num2 = len(text)
target = text[num + 1:num2]
print float(target)