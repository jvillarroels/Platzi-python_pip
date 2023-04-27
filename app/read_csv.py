import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')

        header = next(reader)
        data = []
        # print(header)
        # Esto imprime todo el archivo CSV
        # for row in reader:
        #     print('***' * 5)
        #     print(row)

        for row in reader:
            iterable = zip(header, row)
            # print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            # print(country_dict)
            data.append(country_dict)
        return data
            
           

if __name__ == '__main__':
    data = read_csv('./app/data.csv')    
    print(data[0])

'''
FALTA EL RETO DE LA LECCION 38
Lee un CSV para calcular el total de gastos

'''
    


