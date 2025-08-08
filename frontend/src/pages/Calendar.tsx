import React, { useState } from 'react';
import dayjs from 'dayjs';

const Calendar: React.FC = () => {
  const [currentDate, setCurrentDate] = useState(dayjs());

  const startOfMonth = currentDate.startOf('month');
  const endOfMonth = currentDate.endOf('month');
  const startDay = startOfMonth.day();
  const daysInMonth = currentDate.daysInMonth();

  const generateCalendar = () => {
    const calendar = [];
    let dayCounter = 1;

    for (let week = 0; week < 6; week++) {
      const weekRow = [];
      for (let day = 0; day < 7; day++) {
        if ((week === 0 && day < startDay) || dayCounter > daysInMonth) {
          weekRow.push(<td key={day} className="py-2 px-4 text-gray-300">-</td>);
        } else {
          const isToday =
            dayCounter === dayjs().date() &&
            currentDate.month() === dayjs().month() &&
            currentDate.year() === dayjs().year();

          weekRow.push(
            <td
              key={day}
              className={`py-2 px-4 text-center border rounded ${
                isToday ? 'bg-blue-200 font-bold' : ''
              } hover:bg-blue-100 cursor-pointer`}
            >
              {dayCounter}
            </td>
          );
          dayCounter++;
        }
      }
      calendar.push(<tr key={week}>{weekRow}</tr>);
    }

    return calendar;
  };

  const handlePrev = () => {
    setCurrentDate(currentDate.subtract(1, 'month'));
  };

  const handleNext = () => {
    setCurrentDate(currentDate.add(1, 'month'));
  };

  return (
    <div className="max-w-md mx-auto p-4 bg-white shadow rounded">
      <div className="flex justify-between items-center mb-4">
        <button onClick={handlePrev} className="text-blue-600 font-bold">&lt;</button>
        <h2 className="text-lg font-semibold">{currentDate.format('MMMM YYYY')}</h2>
        <button onClick={handleNext} className="text-blue-600 font-bold">&gt;</button>
      </div>
      <table className="w-full table-fixed">
        <thead>
          <tr>
            {['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'].map((day) => (
              <th key={day} className="py-2 text-gray-600">{day}</th>
            ))}
          </tr>
        </thead>
        <tbody>{generateCalendar()}</tbody>
      </table>
    </div>
  );
};

export default Calendar;