def do_connect():
    import network
    import time
    from time import sleep
    
    t_end = time.time() + 20
    net_name_file = open("nome.txt", "w")
    net_pass_file = open("pass.txt", "w")
    
    
    #connecting to network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        #net_name_file.read() == '' or net_pass_file.read() == ''
        if 1==0:
            network_name = input('Nome da rede: ')
            net_name_file.write(network_name)
            net_name_file.close()
            network_pass = input('Senha: ')
            net_pass_file.write(network_pass)
            net_pass_file.close()
        
        #change_config = input('Change network config? (1 = Yes  ||  0 = No): ')
        change_config = 0
        if change_config == 1:
            network_name = input('Nome da rede: ')
            net_name_file.write(network_name)
            net_name_file.close()
            network_pass = input('Senha: ')
            net_pass_file.write(network_pass)
            net_pass_file.close()   
                      
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(open("nome.txt").read(), open("pass.txt").read())
        while not sta_if.isconnected():
            sleep(2)
            if t_end < time.time():
                break
            
    if sta_if.isconnected() == True:
        print('network config:', sta_if.ifconfig())
    else:
        print('network config:', sta_if.ifconfig())
        print('Unable to connect to wifi, do you want to try again?')
        #try_connect = input('(1 = Yes  ||  0 = No): ')
        try_connect = 0
        if try_connect == 1:
            do_connect()
