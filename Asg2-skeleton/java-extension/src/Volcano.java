import java.util.ArrayList;

public class Volcano extends Mountain {
	private int countdown;
	private int frequency;
	private boolean active;

	public Volcano(int row, int col, int freq) {
		super(row, col);
		this.countdown = freq;
		this.frequency = freq;
		this.color = "\u001b[41m";
		this.active = true;
	}

	public void act(Map map) {
		this.countdown -= 1;
		if (this.countdown == 0) {
			this.countdown = this.frequency;
			ArrayList<Cell> cells = map.getNeighbours(this.row, this.col);
			for (int i = 0; i < cells.size(); ++i) {
				Object occ = cells.get(i).getOccupant();
				if(occ != null) {
					if (occ instanceof GameCharacter) {
						((GameCharacter)occ).setActive(false);
					}
				}
			}
		}
	}

	@Override
	public void display() {
		System.out.format("%s \033[2;97m%d%s \033[0m   ", this.color, this.countdown, this.color);
	}

	// add for java
	public boolean getActive() {
		return this.active;
	}
}