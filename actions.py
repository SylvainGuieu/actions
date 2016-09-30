class Actions(object):
    """ create an action object a list of method to be executed 
    
    action are usualy attached to an other object and executed during
    a specific method. like, e.g. 

        class Rectangle:
            def __init__(self, xy, size):
                self.xy = xy
                self.size = size
                self.on_move = Action()
            def move(self, xy):
                self.xy += xy
                self.on_move.run(self)
            def draw(self):
                # do some drawing    
        
        r = rectangle( (0,0), 1)
        r.on_move.add(  lambda rectangle: rectangle.draw())

    Methods
        add(callable)
            add a new method
        remove(callable)
            remove the method from the list if available
        stop()
            stop any action. run()'s willl have no effect until 
            resume() is called.
        stop(callable)
            stop only the given method
        resume()
            resume everything blocked with run()
        resume(callable)
            resume the callable method blocked with run(method)
        
        run(*args) 
            run all the methods, they should all support the same
            number of arguments.

    """
    _stopped = False
    shape = None

    def __init__(self, actions=[]):
        self.actions = list(actions)
        self.disabled = set([])

    def add(self, func, pos=None):
        """ add a new action method at the end or at pos if provided """
        if not hasattr(func, "__call__"):
            raise ValueError("expecting a callable object got %s"%func)
        
        if pos is None: 
            self.actions.append(func)        
        else:
            self.actions.insert(pos, func) 
       
    def remove(self, func):
        self.actions.remove(func) 

    def stop(self, func=None):
        if func is None:
            self._stopped = True
        else:
            self.disabled.add(func)

    def resume(self, func=None):
        if func is None:
            self._stopped = False
        else:
            try:
                self.disable.remove(func)
            except ValueError:
                pass    

    def run(self, *args):
        if self._stopped:
            return 

        for f in self.actions:
            if f not in self.disabled:
                f(*args)      