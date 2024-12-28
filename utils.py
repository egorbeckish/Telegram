from library import *

def get_coord_distance(distance: str) -> list[int] | tuple[list[int], list[int]]:
	match distance:
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

def get_info_swimmer(distance: str, results: list[str], pdf: str) -> list[str]:
	minim = 1000000
	_results = []

	match distance:
		case '50 Heats':
			for info in results:
				if info.count(' ') != 3:
					info = info.split(maxsplit=2)
					name = info[0]
					surname = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0]
					surname += ' ' + info[2][:index]
					country = info[2][index:index + 3]
					
					_info = info[2][index + 3:].split()
					birthday = f"{_info[0]} {_info[1]} {_info[2][:4]}"
					
					index = 4
					reaction_time = _info[2][index:index + 4]
					_time =  _info[2][index + 4:index + 4 + 5]
					minim = min(minim, float(_time))
					time_behind = str((float(_time) * 100 - minim * 100) / 100)[:4]

				else:
					info = info.split(maxsplit=1)
					name = info[0]
					index = [i for i in range(len(info[1])) if info[1][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[1][:index]
					country = info[1][index:index + 3]

					_info = info[1][index + 3:].split()
					birthday = f"{_info[0]} {_info[1]} {_info[2][:4]}"

					index = 4
					reaction_time = _info[2][index:index + 4]
					_time = _info[2][index + 4:index + 4 + 5]
					minim = min(minim, float(_time))
					time_behind = str((float(_time) * 100 - minim * 100) / 100)[:4]
				
				_results += [[name, surname, country, reaction_time, _time, time_behind]]
			
			return _results
		
		case '50 SemiFinals':
			for info in results:
				if info.count(' ') != 3:
					info = info.split(maxsplit=2)
					name = info[0]
					surname = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0]
					surname += ' ' + info[2][:index]
					country = info[2][index:index + 3]
					
					_info = info[2][index + 3:].split()
					birthday = f"{_info[0]} {_info[1]} {_info[2][:4]}"
					
					index = 4
					reaction_time = _info[2][index:index + 4]
					_time =  _info[2][index + 4:index + 4 + 5]
					minim = min(minim, float(_time))
					time_behind = str((float(_time) * 100 - minim * 100) / 100)[:4]

				else:
					info = info.split(maxsplit=1)
					name = info[0]
					index = [i for i in range(len(info[1])) if info[1][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[1][:index]
					country = info[1][index:index + 3]

					_info = info[1][index + 3:].split()
					birthday = f"{_info[0]} {_info[1]} {_info[2][:4]}"

					index = 4
					reaction_time = _info[2][index:index + 4]
					_time = _info[2][index + 4:index + 4 + 5]
					minim = min(minim, float(_time))
					time_behind = str((float(_time) * 100 - minim * 100) / 100)[:4]
				
				_results += [[name, surname, country, reaction_time, _time, time_behind]]
			
			return _results

		case '50 Final':
			for info in results:
				if info.count(' ') != 1:
					info = info.split(maxsplit=2)
					name = info[0]
					surname = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0]
					surname += ' ' + info[2][:index]
					country = info[2][index:index + 3]
					
					_info = info[2][index + 3:].split()
					index = 4
					reaction_time = _info[2][0:index]
					_time =  _info[2][index:index + 5]
					minim = min(minim, float(_time))
					time_behind = str((float(_time) * 100 - minim * 100) / 100)[:4]
				
				else:
					info = info.split(maxsplit=1)
					name = info[0]
					index = [i for i in range(len(info[1])) if info[1][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[1][:index]
					country = info[1][index:index + 3]
					reaction_time = info[1][index + 3:index + 3 + 4]
					_time = info[1][index + 3 + 4:index + 3 + 4 + 5]
					minim = min(minim, float(_time))
					time_behind = str((float(_time) * 100 - minim * 100) / 100)[:4]
				
				_results += [[name, surname, country, reaction_time, _time, time_behind]]
				
			return _results
		
		case '100 Heats':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split()
				
				first_split = info[0]
				second_split = info[-1]
				tmp = None

				if len(info) != 6:
					difference = len(info) - 6
					name = info[1]
					surname = ' '.join(info[2:2 + difference])
					index = [i for i in range(len(info[3 + difference - 1])) if info[3 + difference - 1][i:i + 3].isupper()][0]
					surname += ' ' + info[3 + difference - 1][:index]
					country = info[3 + difference - 1][index: index + 3]
					birthday = f"{info[3 + difference - 1][index + 3:]} {info[3 + difference]} {info[3 + difference + 1][:4]}"
					reaction_time = info[3 + difference + 1][4:4 + 4]

					_time = info[3 + difference + 1][4 + 4:]
					if ':' in _time:
						tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					
					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str(((float(_time) if not tmp else float(tmp)) * 100 - minim * 100) / 100)[:4]
				
				else:
					name = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[2][:index]
					country = info[2][index:index + 3]
					birthday = f"{info[2][index + 3:]} {info[3]} {info[4][:4]}"
					reaction_time = info[4][4:4 + 4]

					_time = info[4][4 + 4:]
					if ':' in _time:
						tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					
					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str(((float(_time) if not tmp else float(tmp)) * 100 - minim * 100) / 100)[:4]
				
				_results += [[name, surname, country, reaction_time, _time, time_behind, first_split, second_split]]
				
			return _results
			
		case '100 SemiFinals':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split()
				
				first_split = info[0]
				second_split = info[-1]
				tmp = None

				if len(info) != 6:
					difference = len(info) - 6
					name = info[1]
					surname = ' '.join(info[2:2 + difference])
					index = [i for i in range(len(info[3 + difference - 1])) if info[3 + difference - 1][i:i + 3].isupper()][0]
					surname += ' ' + info[3 + difference - 1][:index]
					country = info[3 + difference - 1][index: index + 3]
					birthday = f"{info[3 + difference - 1][index + 3:]} {info[3 + difference]} {info[3 + difference + 1][:4]}"
					reaction_time = info[3 + difference + 1][4:4 + 4]

					_time = info[3 + difference + 1][4 + 4:]
					if ':' in _time:
						tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					
					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str(((float(_time) if not tmp else float(tmp)) * 100 - minim * 100) / 100)[:4]
					
				
				else:
					name = info[1]						
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[2][:index]
					country = info[2][index:index + 3]
					birthday = f"{info[2][index + 3:]} {info[3]} {info[4][:4]}"
					reaction_time = info[4][4:4 + 4]

					_time = info[4][4 + 4:]
					if ':' in _time:
						tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					
					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str(((float(_time) if not tmp else float(tmp)) * 100 - minim * 100) / 100)[:4]
			
				_results += [[name, surname, country, reaction_time, _time, time_behind, first_split, second_split]]
			
			return _results 		
		
		case '100 Final':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split()
				info.pop(0)

				first_split = info[0]
				second_split = info[-1]
				tmp = None

				if len(info) != 4:
					difference = len(info) - 4
					name = info[1]
					surname = ' '.join(info[2:2 + difference])
					index = [i for i in range(len(info[3 + difference - 1])) if info[3 + difference - 1][i:i + 3].isupper()][0]
					surname += ' ' + info[3 + difference - 1][:index]
					country = info[3 + difference - 1][index: index + 3]
					reaction_time = info[3 + difference - 1][index + 3:index + 3 + 4]

					_time = info[3 + difference - 1][index + 3 + 4:index + 3 + 4 + 5] if ':' not in info[3 + difference - 1] else info[3 + difference - 1][index + 3 + 4:index + 3 + 4 + 8]
					if ':' in _time:
						tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
						#_time = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					
					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str(((float(_time) if not tmp else float(tmp)) * 100 - minim * 100) / 100)[:4]
				
				else:
					name = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[2][:index]
					country = info[2][index: index + 3]
					reaction_time = info[2][index + 3:index + 3 + 4]

					_time = info[2][index + 3 + 4:index + 3 + 4 + 5] if ':' not in info[2] else info[2][index + 3 + 4:index + 3 + 4 + 8]
					if ':' in _time:
						tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
						#_time = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))

					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str(((float(_time) if not tmp else float(tmp)) * 100 - minim * 100) / 100)[:4]
			
				_results += [[name, surname, country, reaction_time, _time, time_behind, first_split, second_split]]

			return _results

		case '200 Heats':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split()

				_split = ' '.join([info[0][:5], info[-1][:5], info[-1][5:5 + 5], info[-1][5 + 5:]])
				if len(info) != 6:
					difference = len(info) - 6
					name = info[1]
					surname = ' '.join(info[2:2 + difference])
					index = [i for i in range(len(info[3 + difference - 1])) if info[3 + difference - 1][i:i + 3].isupper()][0]
					surname += ' ' + info[3 + difference - 1][:index]
					country = info[3 + difference - 1][index: index + 3]
					birthday = f"{info[3 + difference - 1][index + 3:]} {info[3 + difference]} {info[3 + difference + 1][:4]}"
					reaction_time = info[3 + difference + 1][4:4 + 4]
					_time = info[3 + difference + 1][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
				
				else:
					name = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[2][:index]
					country = info[2][index:index + 3]
					birthday = f"{info[2][index + 3:]} {info[3]} {info[4][:4]}"
					reaction_time = info[4][4:4 + 4]
					_time = info[4][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]

				_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results

		case '200 SemiFinals':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split()

				_split = ' '.join([info[0][:5], info[-1][:5], info[-1][5:5 + 5], info[-1][5 + 5:]])
				if len(info) != 6:
					difference = len(info) - 6
					name = info[1]
					surname = ' '.join(info[2:2 + difference])
					index = [i for i in range(len(info[3 + difference - 1])) if info[3 + difference - 1][i:i + 3].isupper()][0]
					surname += ' ' + info[3 + difference - 1][:index]
					country = info[3 + difference - 1][index: index + 3]
					birthday = f"{info[3 + difference - 1][index + 3:]} {info[3 + difference]} {info[3 + difference + 1][:4]}"
					reaction_time = info[3 + difference + 1][4:4 + 4]
					_time = info[3 + difference + 1][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(_time) if not tmp else float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
				
				else:
					name = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[2][:index]
					country = info[2][index:index + 3]
					birthday = f"{info[2][index + 3:]} {info[3]} {info[4][:4]}"
					reaction_time = info[4][4:4 + 4]
					_time = info[4][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]

				_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results

		case '200 Final':
			for i in range(0, len(results) - len(results) % 3, 3):
				info = ' '.join(results[i: i + 3]).split()
				info.pop(0)

				for _ in range(2):
					info.pop(1)
				
				_split = ' '.join([info[0][:5], info[-1][:5], info[-1][5:5 + 5], info[-1][5 + 5:]])

				if len(info) != 4:
					difference = len(info) - 4
					name = info[1]
					surname = ' '.join(info[2:2 + difference])
					index = [i for i in range(len(info[3 + difference - 1])) if info[3 + difference - 1][i:i + 3].isupper()][0]
					surname += ' ' + info[3 + difference - 1][:index]
					country = info[3 + difference - 1][index:index + 3]
					reaction_time = info[3 + difference - 1][index + 3:index + 3 + 4]
					_time = info[3 + difference - 1][index + 3 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
				
				else:
					name = info[1]
					index = [i for i in range(len(info[2])) if info[2][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[2][:index]
					country = info[2][index:index + 3]
					reaction_time = info[2][index + 3:index + 3 + 4]
					_time = info[2][index + 3 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]

				_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			if len(results) % 3:
				for i in range(len(results) - len(results) % 3, len(results)):
					info = results[i].split()
					name = info[0]
					index = [i for i in range(len(info[1])) if info[1][i:i + 3].isupper()][0] if name != 'HAUGHEY' else 2
					surname = info[1][:index]
					country = info[1][index:index + 3]
					_time = info[1][index + 3:]
					_results += [[name, surname, country, '', _time, '', '']]
			
			return _results

		case '400 Heats':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split(maxsplit=4)

				_split = ' '.join([(tmp:=info[-1].split())[1 if ':' in info[3] else 2][:5]] + [tmp[-1][i:i + 5] for i in range(0, len(tmp[-1]), 5)])
				if len(info) != 5 or ':' not in info[3]:
					name = info[0][re.search(r'[A-Z]', info[0]).start():]
					surname = info[1]
					index = re.search(r'[\d]', info[2]).start()
					surname += ' ' + info[2][:index - 3]
					country = info[2][index - 3:index]
					birthday = f'{info[2][index:]} {info[3]} {info[4][:4]}'
					reaction_time = info[4][4:4 + 4]
					_time = info[4].split()[0][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
				
				else:
					name = info[0][re.search(r'[A-Z]', info[0]).start():]
					index = re.search(r'[\d]', info[1]).start()
					surname = info[1][:index - 3]
					country = info[1][index - 3:index]
					birthday = f'{info[1][index:]} {info[2]} {info[3][:4]}'
					reaction_time = info[3][4:4 + 4]
					_time = info[3][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results
		
		case '400 Final':
			for i in range(0, len(results), 3):
				info = ' '.join(results[i: i + 3]).split(maxsplit=2)

				_split = ' '.join([(tmp:=info[-1].split())[2 if ':' in info[1] else 3][:5]] + [tmp[-1][i:i + 5] for i in range(0, len(tmp[-1]), 5)])
				name = info[0][re.search(r'[A-Z]', info[0]).start():]
				if len(info) != 3 or ':' not in info[1]:
					surname = info[1]
					index = re.search(r'[\d]', info[2]).start()
					surname += ' ' + info[2][:index - 3]
					country = info[2][index - 3:index]
					reaction_time = info[2][index:index + 4]
					_time = info[2][index + 4:index + 4 + 7]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
				
				else:
					index = re.search(r'[\d]', info[1]).start()
					surname = info[1][:index - 3]
					country = info[1][index - 3:index]
					reaction_time = info[1][index:index + 4]
					_time = info[1][index + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results

		case '800 Heats':
			for i in range(0, len(results), 5):
				info = ' '.join(results[i: i + 5]).split(maxsplit=4)
				
				_split = ' '.join([(tmp:=info[-1].split())[1 if ':' in info[3] else 2][:5]] + \
						[tmp[9 if ':' in info[3] else 10][i:i + 5] for i in range(0, len(tmp[9 if ':' in info[3] else 10]), 5)] + \
						[tmp[-1][i:i + 5] for i in range(0, len(tmp[-1]), 5)])
				
				if len(info) != 5 or ':' not in info[3]:
					name = info[0][re.search(r'[0-9]+', info[0]).end():]
					surname = info[1]
					index = re.search(r'[\d]', info[2]).start()
					surname += ' ' + info[2][:index - 3]
					country = info[2][index - 3:index]
					birthday = f'{info[2][index:]} {info[3]} {info[4][:4]}'
					reaction_time = info[4][4:4 + 4]
					_time = info[4].split()[0][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]

				
				else:
					name = info[0][re.search(r'[A-Z]', info[0]).start():]
					index = re.search(r'[\d]', info[1]).start()
					surname = info[1][:index - 3]
					country = info[1][index - 3:index]
					birthday = f'{info[1][index:]} {info[2]} {info[3][:4]}'
					reaction_time = info[3][4:4 + 4]
					_time = info[3][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results

		case '800 Final':
			for i in range(0, len(results), 5):
				info = ' '.join(results[i: i + 5]).split(maxsplit=2)
				
				_split = ' '.join([(tmp:=info[-1].split())[2 if ':' not in tmp[0] else 3][:5]] + \
						[tmp[17 if ':' not in tmp[0] else 18][i:i + 5] for i in range(0, len(tmp[17 if ':' not in tmp[0] else 18]), 5)] + \
						[tmp[-1][i:i + 5] for i in range(0, len(tmp[-1]), 5)])

				if len(info) != 3 or ':' not in info[1]:
					name = info[0][re.search(r'[0-9]+', info[0]).end():]
					surname = info[1]
					index = re.search(r'[A-Z]{3}', info[2]).start()
					surname += ' ' + info[2][:index]
					country = (tmp:=info[2].split())[0][index:index + 3]
					reaction_time = tmp[0][index + 3:index + 3 + 4]
					_time = tmp[0][index + 3 + 4:index + 3 + 4 + 7]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]

					
				
				else:
					name = info[0][re.search(r'[0-9]+', info[0]).end():]
					index = re.search(r'[A-Z]{3}', info[1]).start()
					surname = info[1][:index]
					country = info[1][index:index + 3]
					reaction_time = info[1][index + 3:index + 3 + 4]
					_time = info[1][index + 3 + 4:index + 3 + 4 + 7]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results

		case '1500 Heats':
			for i in range(0, len(results), 9):
				info = ' '.join(results[i: i + 9]).split(maxsplit=4)

				_split = ' '.join([(tmp:=info[-1].split())[1 if ':' in info[3] else 2][:5]] + \
						[tmp[9 if ':' in info[3] else 10][i:i + 5] for i in range(0, len(tmp[9 if ':' in info[3] else 10]), 5)] + \
						[tmp[19 if ':' in info[3] else 20][i:i + 5] for i in range(0, len(tmp[19 if ':' in info[3] else 20]), 5)] + \
						[tmp[29 if ':' in info[3] else 30][i:i + 5] for i in range(0, len(tmp[29 if ':' in info[3] else 30]), 5)] + \
						[tmp[-1][i:i + 5] for i in range(0, len(tmp[-1]), 5)])
				
				if len(info) != 5 or ':' not in info[3]:
					name = info[0][re.search(r'[0-9]+', info[0]).end():]
					surname = info[1]
					index = re.search(r'[\d]', info[2]).start()
					surname += ' ' + info[2][:index - 3]
					country = info[2][index - 3:index]
					birthday = f'{info[2][index:]} {info[3]} {info[4][:4]}'
					reaction_time = info[4][4:4 + 4]
					_time = info[4].split()[0][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:5]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
				
				else:
					name = info[0][re.search(r'[0-9]+', info[0]).end():]
					index = re.search(r'[A-Z]{3}', info[1]).start()
					surname = info[1][:index]
					country = info[1][index:index + 3]
					birthday = f'{info[1][index + 3:]} {info[2]} {info[3][:4]}'
					reaction_time = info[3][4:4 + 4]
					_time = info[3][4 + 4:]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:4]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]

			return _results
		
		case '1500 Final':
			for i in range(0, len(results), 9):
				info = ' '.join(results[i: i + 9]).split(maxsplit=2)
				
				_split = ' '.join([(tmp:=info[-1].split())[2][:5]] + \
						[tmp[17 if ':' not in tmp[0] else 18][i:i + 5] for i in range(0, len(tmp[17 if ':' not in tmp[0] else 18]), 5)] + \
						[tmp[35 if ':' not in tmp[0] else 36][i:i + 5] for i in range(0, len(tmp[35 if ':' not in tmp[0] else 36]), 5)] + \
						[tmp[53 if ':' not in tmp[0] else 54][i:i + 5] for i in range(0, len(tmp[53 if ':' not in tmp[0] else 54]), 5)] + \
						[tmp[-1][i:i + 5] for i in range(0, len(tmp[-1]), 5)])

				if len(info) != 3:
					...
				
				else:
					name = info[0][re.search(r'[0-9]+', info[0]).end():]
					index = re.search(r'[A-Z]{3}', info[1]).start()
					surname = info[1][:index]
					country = info[1][index:index + 3]
					reaction_time = info[1][index + 3:index + 3 + 4]
					_time = info[1][index + 3 + 4:index + 3 + 4 + 8]
					tmp = str(float(_time[:_time.index(':')]) * 60 + float(_time[_time.index(':') + 1:]))
					minim = min(minim, float(tmp))
					time_behind = str((float(tmp) * 100 - minim * 100) / 100)[:5]
					_results += [[name, surname, country, reaction_time, _time, time_behind, _split]]
			
			return _results

		
def get_results(pdf: str):
	distance = f"{pdf.split('/')[1].split()[0]} {pdf.split('/')[1].split()[-1].split('.')[0]}"
	coords = get_coord_distance(distance)
	_pdf = HotPdf(open(pdf, 'rb'))

	match distance:
		case '50 Heats':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)
		
		case '50 SemiFinals':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '50 Final':
			results = list(map(lambda x: x.replace('\n', '', 1), _pdf.extract_text(*coords).split(' \n')))
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)
		
		case '100 Heats':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)
		
		case '100 SemiFinals':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)
		
		case '100 Final':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '200 Heats':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '200 SemiFinals':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '200 Final':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '400 Heats':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '400 Final':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '800 Heats':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		case '800 Final':
			results = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)
		
		case '1500 Heats':
			results: list[str] = _pdf.extract_text(*coords[0]).split('\n')
			results.pop(-1)
			results += _pdf.extract_text(*coords[1], 1).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)
		
		case '1500 Final':
			results: list[str] = _pdf.extract_text(*coords).split('\n')
			results.pop(-1)
			return get_info_swimmer(distance, results, pdf)

		
def get_pdf():
	return os.listdir('World Cup I Stage 18.10-20.10.2024')

def print_results(el):
	return '\n'.join(list(map(lambda x: ' '.join(x), el)))