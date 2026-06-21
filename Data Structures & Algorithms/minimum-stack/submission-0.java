class MinStack {
    List<Integer> minStack = new ArrayList();;
    public MinStack() {
    }
    
    public void push(int val) {
        minStack.add(val);
    }
    
    public void pop() {
        minStack.remove(minStack.size()-1);
    }
    
    public int top() {
        return minStack.get(minStack.size()-1);
    }
    
    public int getMin() {
        int min = minStack.get(0);
        for (int s : minStack) {
            if (s < min) {
                min = s;
                }
            }
        return min;
    }
}
