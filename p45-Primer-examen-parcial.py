# Cálculo de costo para inscripción

import os
vt = 0
while True:
   os.system("cls")
   
   print("Indique el tipo de usuario:")
   print(" [ 1 ] Alumno     $100.00 ")
   print(" [ 2 ] Trabajador $200.00")
   print(" [ 3 ] Docente    $500.00")
   tu = int(input("Elige."))

   print("Indique el paquete deseado:")
   print(" [ 1 ] Solo conferencias     $600.00 ")
   print(" [ 2 ] Con eventos sociales  $800.00")
   print(" [ 3 ] Con kit de acceso     $900.00")
   tp = int(input("Elige."))

   print("Indique la cantidad:")
   cant = int(input("Elige."))
   

   if tu == 1:
    if tp==1:
        costo=(cant*100)+(cant*600)
        if costo > 5000:
            descuento=costo*.2
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
    elif tp==2:
        costo=(cant*100)+(cant*800)
        if costo > 5000:
            descuento=costo*.2
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
    elif tp==3:
        costo=(cant*100)+(cant*900)
        if costo > 5000:
            descuento=costo*.2
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"Subtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
    else:
        print("ERROR en captura de datos.")  
   elif tu == 2:
        if tp==1:
           costo=(cant*200)+(cant*600)
           if costo > 5000:
            descuento=costo*.1
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
           else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        elif tp==2:
           costo=(cant*200)+(cant*800)
           if costo > 5000:
            descuento=costo*.1
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
           else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        elif tp==3:
           costo=(cant*200)+(cant*900)
           if costo > 5000:
            descuento=costo*.1
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
           else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"Subtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")  
   elif tu == 3:
        if tp==1:
           costo=(cant*500)+(cant*600)
           if costo > 5000:
            descuento=costo*.05
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
           else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        elif tp==2:
           costo=(cant*500)+(cant*800)
           if costo > 5000:
            descuento=costo*.05
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
           else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
        elif tp==3:
           costo=(cant*500)+(cant*900)
           if costo > 5000:
            descuento=costo*.05
            costof=costo-descuento
            vt = vt+costof
            print(f"\nSubtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")
           else:
            descuento=0
            costof=costo
            vt = vt+costof
            print(f"Subtotal     ${costo:,.2f}")
            print(f"Descuento   -${descuento:,.2f}")
            print(f"Total        ${costof:,.2f}")


   if input("Deseas continuar (S/N)").upper().startswith("N"):break
print(f"\nImporte total de la venta: ${vt:,.2f}")
print("\nProceso terminado...")