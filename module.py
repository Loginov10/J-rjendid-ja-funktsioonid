def kool(opilased,puudumised,komissoin):
    """
    """
    a=int(input("Mitu õpilased sa tahad lisada? "))
    for i in range(a):
        b=input("Sisestage nimi: ")
        if b not in opilased:
            c=input("Sisestage tema puudumised: ")       
            bb=opilased.append(b)
            cc=puudumised.append(c)
        else:
            print("!!!!")
        print(opilased,puudumised)     
        return bb,cc
    
        m=min(puudumised)
        c=sorted(m)
        print(opilased,puudumised)
        return c
    
        list(reversed(sorted(reversed(m))))
        print(opilased+\n puuduimised)

        print("opilased kes läheb komissionil: ")
        if puudumised>50:
            index=opilased.index()
            komission.append(index)
            print(komission)
        else:
            print("!!!")

        print("opilased kes eemalda järjendest ")
        if puudumised>100:
            index=puudumised.index()
            opilased.pop(index)
            puudumised.pop(index)
            print(opilased,puudumised)
            return opilased, puudumised
        else:
             print("!!!!")
    
    
 
            

        


