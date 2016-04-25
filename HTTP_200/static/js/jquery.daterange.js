/**
 * jQuery UI Datepicker add-on which can help select date range
 * First click selects start date of range. Second click selects
 * end date of range and closes calendar.
 *
 * Plugin accept all Datepicker options. Also, plugin introduce one more
 * option -- rangeSeparator.
 *
 * http://noteskeeper.ru/38/
 *
 * Copyright 2009-2013 Vladimir Kuznetsov <mistakster@gmail.com>
 * Released under the MIT license
 * http://opensource.org/licenses/MIT
 *
 */
(function ($) {

  function compareDates(start, end, format) {
    var temp, dateStart, dateEnd;

    try {
      dateStart = $.datepicker.parseDate(format, start);
      dateEnd = $.datepicker.parseDate(format, end);
      if (dateEnd < dateStart) {
        temp = start;
        start = end;
        end = temp;
      }
    } catch (ex) {}

    return { start: start, end: end };
  }

  $.fn.daterange = function (opts) {

    // defaults
    opts = $.extend({
      "changeMonth": false,
      "changeYear": false,
      "numberOfMonths": 2,
      "rangeSeparator": " - "
    }, opts || {});

    var onSelect = opts.onSelect || $.noop;
    var onClose = opts.onClose || $.noop;
    var beforeShow = opts.beforeShow || $.noop;
    var beforeShowDay = opts.beforeShowDay;

    var lastDateRange;

    function storeLastDateRange(dateText, dateFormat) {
      var start, end;
      dateText = dateText.split(opts.rangeSeparator);
      if (dateText.length > 0) {
        start = $.datepicker.parseDate(dateFormat, dateText[0]);
        if (dateText.length > 1) {
          end = $.datepicker.parseDate(dateFormat, dateText[1]);
        }
        lastDateRange = {start: start, end: end};
      } else {
        lastDateRange = null;
      }
    }

    opts.beforeShow = function (input, inst) {
      // store dateText to highlight it latter
      var dateFormat = $(this).datepicker("option", "dateFormat");
      storeLastDateRange($(input).val(), dateFormat);
      beforeShow.apply(this, arguments);
    };

    opts.beforeShowDay = function (date) {

      var out = [true, ""], extraOut;

      if (lastDateRange && lastDateRange.start <= date) {
        if (lastDateRange.end && date <= lastDateRange.end) {
          out[1] = "ui-datepicker-range";
        }
      }

      if (beforeShowDay) {
        extraOut = beforeShowDay.apply(this, arguments);
        out[0] = out[0] && extraOut[0];
        out[1] = out[1] + " " + extraOut[1];
        out[2] = extraOut[2];
      }

      return out;
    };

    // datepicker's select date event handler
    opts.onSelect = function (dateText, inst) {
      var textStart;
      if (!inst.rangeStart) {
        inst.inline = true;
        inst.rangeStart = dateText;
      } else {
        inst.inline = false;
        textStart = inst.rangeStart;
        if (textStart !== dateText) {
          var dateFormat = $(this).datepicker("option", "dateFormat");
          var dateRange = compareDates(textStart, dateText, dateFormat);
          $(this).val(dateRange.start + opts.rangeSeparator + dateRange.end);
          inst.rangeStart = null;
        }
      }
      // call original callback for select event
      onSelect.apply(this, arguments);
    };

    opts.onClose = function (dateText, inst) {
      // reset state
      inst.rangeStart = null;
      inst.inline = false;
      // call original callback for close event
      onClose.apply(this, arguments);
    };

    return this.each(function () {
      var input = $(this);
      if (input.is("input")) {
        input.datepicker(opts);
      }
    });
  };

}(jQuery));