class MinStack {
    List<Integer> minStack;
    List<Integer> stack;
    public MinStack() {
        minStack = new ArrayList();
        stack = new ArrayList();
    }
    
    public void push(int val) {
        minStack.add(val);
        if(stack.size()>0){
            int min = stack.get(stack.size()-1);
            if(val<min)
            min = val;
            stack.add(min);
        } else {
            stack.add(val);
        }
        
    }
    
    public void pop() {
        minStack.remove(minStack.size()-1);
        stack.remove(stack.size()-1);
    }
    
    public int top() {
        return minStack.get(minStack.size()-1);
    }
    
    public int getMin() {
        return stack.get(stack.size()-1);
    }
}
