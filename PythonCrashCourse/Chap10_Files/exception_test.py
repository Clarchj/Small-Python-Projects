def askTwoNumber():
        while True:
                print('asking for 2 numbers, press \'q\' to quit')
                x = input('please give me the firs tnumber')
                if x == 'q':
                        break
                y =  input('please give me the second number')
                if y == 'q':
                        break
                try: 
                        sum_result = int(x) + int(y)  
                except (TypeError,ValueError):
                        error_msg = 'sorry, the input have to be numbers'
                        print(error_msg)
                else: 
                        print(sum_result)
                

askTwoNumber()
                