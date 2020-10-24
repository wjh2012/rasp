def pwm(m):
    for key in led.keys():
        GPIO.output(key,False)
            
    pwm_r = GPIO.PWM(16,500)
    pwm_r.start(0)

    pwm_g = GPIO.PWM(20,500)
    pwm_g.start(0)

    pwm_b = GPIO.PWM(21,500)
    pwm_b.start(0)
    
    while m==True:
        try:
            for i in range(101):
                if(i==100):
                    i=0
                    
                if led[16] == True:
                    pwm_r.ChangeDutyCycle(i)
                    
                if led[20] == True:
                    pwm_g.ChangeDutyCycle(i)
                    
                if led[21] == True:
                    pwm_b.ChangeDutyCycle(i)
            
                time.sleep(0.02)
        
        except KeyboardInterrupt:
            pwm_r.ChangeDutyCycle(0)
            pwm_g.ChangeDutyCycle(0)
            pwm_b.ChangeDutyCycle(0)
            
            for key in led.keys():
                led[key]=False
            
            break