class DriveThread extends Thread{

	public DriveThread() {
		super();
		this.setName("DriveThread");
	}
	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("This is the DriveThread Executing");
	}

	
}
class InputThread extends Thread {

	public InputThread() {
		super();
		this.setName("InputThread");
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("This is the InputThread Executing");
		
	}
	
}
class OpticalThread extends Thread{

	public OpticalThread() {
		super();
		this.setName("OpticalThread");
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("This is the OpticalThread Executing");
		
	}
	
}
class SandSortingThread extends Thread{

	public SandSortingThread() {
		super();
		this.setName("SandSortingThread");
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("This is the SandSortingThread Executing");
		
	}
	
}
