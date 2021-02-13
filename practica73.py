def run():
    queue = []
    while True:
        queue.append(str(input("Ingresa tu nombre: ")))
        print(f"Ha ingresado :{queue} a nuestra cola")
        if len(queue) == 2:
            break
    if any(queue):
        i = queue.pop(0)
        print(f"Ha sido atentido el cliente: {i}")
        print(queue)
if __name__ == "__main__":
    run()