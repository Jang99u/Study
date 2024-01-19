public class Sequence {
    private int[] values;

    public Sequence(int size) {
        values = new int[size];
    }

    public void set(int i, int n) {
        values[i] = n;
    }

    public int get(int i) {
        return values[i];
    }

    public int size() {
        return values.length;
    }

    public boolean equals(Sequence arr) {
        int arrlen = arr.size();
        if(values.length != arrlen) return false;

        for(int i = 0; i < arrlen; i++) {
            if(values[i] != arr.get(i)) return false;
        }
        return true;
    }
}