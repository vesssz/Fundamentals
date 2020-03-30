def decipher(message):
    data = message.split("&")
    treasure = data[1]
    data2 = data[-1]
    start_index = data2.index("<")
    end_index = data2.index(">")
    coordinates = data2[start_index + 1:end_index]

    result = {treasure: coordinates}
    return result
print(decipher("hidden&gold&at<10N70W>"))
