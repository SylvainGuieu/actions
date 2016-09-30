actions module is a one object module. The oject is called Actions 

It provide a way to attach some actions to be executed withon an object method.

For instance:

        class Rectangle:
            def __init__(self, xy, size):
                self.xy = xy
                self.size = size
                self.on_move = Action()
            def move(self, xy):
                self.xy += xy
                self.on_move.run(self)
            def draw(self):
                # do some rectangle drawing    
        
        r = rectangle( (0,0), 1)
        r.on_move.add(  lambda r: r.draw())        


The class has the following methods

- add(callable)  
    add a new method

- remove(callable)  
    remove the method from the list if available

- stop()  
    stop any action. run()'s willl have no effect until 
    resume() is called.

- stop(callable)  
    stop only the given method

- resume()  
    resume everything blocked with run()

- resume(callable)  
    resume the callable method blocked with stop(method)

- run(*args)   
    run all the methods, they should all support the same
    number of arguments.

