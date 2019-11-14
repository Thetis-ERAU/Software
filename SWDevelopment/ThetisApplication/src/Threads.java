/**
 * DriveThread controls all motor operations
 * 
 * @author ProjectThetis
 *
 */
class ThreadBase {
	class DriveThread extends Thread {
		protected Systems.DriveSystem driveSystem;

		public DriveThread() {
			super();
			driveSystem = new Systems.DriveSystem();
			setName("DriveThread");
		}

		@Override
		public void run() {
			// TODO Auto-generated method stub
			System.out.println("This is the DriveThread Executing");
		}

	}

	/**
	 * InputThread contains all GPS, Accel, ect. reads
	 * 
	 * @author ProjectThetis
	 *
	 */
	class InputThread extends Thread {
		protected Systems.InputSystem inputSystem;

		public InputThread() {
			super();
			inputSystem = new Systems.InputSystem();
			setName("InputThread");
		}

		@Override
		public void run() {
			// TODO Auto-generated method stub
			System.out.println("This is the InputThread Executing");

		}

	}

	/**
	 * OpticalThread contains all Lidar and camera detection and operation functions
	 * 
	 * @author ProjectThetis
	 *
	 */
	class OpticalThread extends Thread {
		protected Systems.OpticalSystem opticalSystem;

		public OpticalThread() {
			super();
			opticalSystem = new Systems.OpticalSystem();
			this.setName("OpticalThread");
		}

		@Override
		public void run() {
			// TODO Auto-generated method stub
			System.out.println("This is the OpticalThread Executing");

		}

	}

	/**
	 * SandSortingThread controls the internal sorting functions
	 * 
	 * @author ProjectThetis
	 *
	 */
	class SandSortingThread extends Thread {
		protected Systems.SandSortingSystem sortingSystem;

		public SandSortingThread() {
			super();
			sortingSystem = new Systems.SandSortingSystem();
			this.setName("SandSortingThread");
		}

		@Override
		public void run() {
			// TODO Auto-generated method stub
			System.out.println("This is the SandSortingThread Executing");

		}
	}
}
