import {Story, Meta} from '@storybook/react/types-6-0';

import {CardPrice, CardPriceProps} from './CardPrice';

export default {
    title: 'Components/Card',
    component: CardPrice
} as Meta;

const Template: Story<CardPriceProps> = (args) => <CardPrice {...args} />

export const Price = Template.bind({});
Price.args = {
    description: 'Description',
    itemType: 'Item type',
    quantity: 2,
    price: 99900
}