class Pool_50m:
	def __init__(self, filename: str) -> None:
		self.__filename: str = filename
		self.__distance: str = f'{(tmp:=filename.split())[0]} {tmp[-1].split('.')[0]}'
		self.__style: str = tmp[1]
		self.__sex: str = tmp[2]
	
	@property
	def filename(self) -> str:
		return self.__filename
	
	@property
	def distance(self) -> str:
		return self.__distance
	
	@property
	def style(self) -> str:
		return self.__style
	
	@property
	def sex(self) -> str:
		return self.__sex
	
	@property
	def coords_distance(self) -> list[int] | tuple[list[int], list[int]]:
		match self.distance:
			case '50 Heats':
				return [110, 250, 490, 450]

			case '50 SemiFinals':
				return [110, 250, 490, 360]
			
			case '50 Final':
				return [110, 250, 490, 340]
			
			case '100 Heats':
				return [105, 250, 490, 610]

			case '100 SemiFinals':
				return [105, 250, 490, 450]
			
			case '100 Final':
				return [118, 250, 490, 410]
			
			case '200 Heats':
				return [100, 250, 500, 610]

			case '200 SemiFinals':
				return [100, 250, 500, 445]
			
			case '200 Final':
				return [80, 250, 525, 450]
			
			case '400 Heats':
				return [0, 250, 510, 530]
			
			case '400 Final':
				return [0, 250, 510, 480]
			
			case '800 Heats':
				return [0, 250, 510, 690]
			
			case '800 Final':
				return [0, 250, 510, 690]
			
			case '1500 Heats':
				return [0, 250, 510, 730], [0, 200, 510, 510]
			
			case '1500 Final':
				return [0, 250, 525, 730]
			